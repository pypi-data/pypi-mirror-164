#ifndef MC_UNIVERSE_GENERATOR_H
#define MC_UNIVERSE_GENERATOR_H

#include "../entities/Atom.h"
#include "../entities/Box.h"
#include "../entities/Universe.h"
#include "StringUtils.h"
#include <algorithm>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <math.h>/* isnan, sqrt */
#include <string>
#include <vector>
#ifndef M_PI
#define M_PI 3.1415926535897932384626433
#endif

#include <random>

namespace pylimer_tools {
namespace utils {

  struct Positions
  {
    std::vector<double> x;
    std::vector<double> y;
    std::vector<double> z;
  };

  struct SimplifiedUniverse
  {
    std::vector<long int> ids;
    std::vector<int> types;
    std::vector<double> x;
    std::vector<double> y;
    std::vector<double> z;
    std::vector<long int> bondsFrom;
    std::vector<long int> bondsTo;
  };

  class MCUniverseGenerator
  {
  public:
    MCUniverseGenerator(const double Lx, const double Ly, const double Lz)
    {
      std::random_device rd {};
      this->rng = std::mt19937(rd());
      this->distX = std::uniform_real_distribution<double>(0.0, Lx);
      this->distY = std::uniform_real_distribution<double>(0.0, Ly);
      this->distZ = std::uniform_real_distribution<double>(0.0, Lz);
      this->distSelect = std::uniform_real_distribution<double>(0.0, 1.0);
      this->box = pylimer_tools::entities::Box(Lx, Ly, Lz);
    }
    
    void setSeed(unsigned int seed) { this->rng.seed(seed); };

    void setBeadDistance(double newBeadDistance)
    {
      this->beadDistance = newBeadDistance;
    };

    pylimer_tools::entities::Universe getUniverse()
    {
      pylimer_tools::entities::Universe universe =
        pylimer_tools::entities::Universe(this->box);
      int nrOfAtoms = this->simplifiedUniverse.ids.size();
      std::vector<int> zeros = initializeWithValue(nrOfAtoms, 0);
      universe.addAtoms(nrOfAtoms,
                        this->simplifiedUniverse.ids,
                        this->simplifiedUniverse.types,
                        this->simplifiedUniverse.x,
                        this->simplifiedUniverse.y,
                        this->simplifiedUniverse.z,
                        zeros,
                        zeros,
                        zeros);
      universe.addBonds(this->simplifiedUniverse.bondsFrom,
                        this->simplifiedUniverse.bondsTo);
      return universe;
    };

    void addCrosslinkers(int nrOfCrosslinkers, int crosslinkerAtomType = 2)
    {
      if (this->crosslinkerType != crosslinkerAtomType) {
        if (this->crosslinkerType != 0) {
          throw std::invalid_argument(
            "Crosslinkers must all have the same type.");
        }
        this->crosslinkerType = crosslinkerAtomType;
      }
      std::vector<size_t> newCrosslinkerIdxs =
        this->addAtomsWithType(nrOfCrosslinkers, crosslinkerAtomType);
      this->crosslinkerIdxs.reserve(this->crosslinkerIdxs.size() +
                                    newCrosslinkerIdxs.size());
      this->crosslinkerIdxs.insert(this->crosslinkerIdxs.end(),
                                   newCrosslinkerIdxs.begin(),
                                   newCrosslinkerIdxs.end());
    };

    /**
     * @brief Randomly distribute
     *
     * @param nrOfSolventChains
     * @param chainLength
     * @param solventAtomType
     */
    void addSolventChains(int nrOfSolventChains,
                          int chainLength,
                          int solventAtomType = 3)
    {
      // std::cout << "Adding " << nrOfSolventChains << " atoms for solvent
      // chains."
      //           << std::endl;
      std::vector<size_t> startAtoms =
        this->addAtomsWithType(nrOfSolventChains, solventAtomType);

      for (size_t atomIdx : startAtoms) {
        // std::cout << "Adding solvent chain with length " << chainLength
        //           << std::endl;
        this->addRandomWalkChainFrom(atomIdx, chainLength - 1, solventAtomType);
      }
    };

    /**
     * @brief Add strands in between the cross-linkers, link them as appropriate
     *
     * @param nrOfStrands the nr. of Strands to add
     * @param beadsPerChains the nr. of beads per strand (excl. cross-linkers)
     * @param crosslinkerConversion "p", the target conversion of the
     * cross-linkers
     * @param crosslinkerFunctionality the functionality of the cross-linker
     * beads to add
     * @param strandAtomType the type of the strand atoms
     */
    void addAndLinkStrands(int nrOfStrands,
                           std::vector<int> beadsPerChains,
                           double crosslinkerConversion,
                           int crosslinkerFunctionality = 4,
                           int strandAtomType = 1)
    {
      if (beadsPerChains.size() != nrOfStrands) {
        throw std::invalid_argument("Nr of strands must be equal to the number "
                                    "of chainLengths provided.");
      }

      // eager reserve of vectors
      // could be more elaborate, but with a certain probability,
      // this is better
      this->simplifiedUniverse.ids.reserve(this->simplifiedUniverse.ids.size() +
                                           nrOfStrands * beadsPerChains[0]);
      this->simplifiedUniverse.types.reserve(
        this->simplifiedUniverse.types.size() +
        nrOfStrands * beadsPerChains[0]);

      this->simplifiedUniverse.x.reserve(this->simplifiedUniverse.x.size() +
                                         nrOfStrands * beadsPerChains[0]);
      this->simplifiedUniverse.y.reserve(this->simplifiedUniverse.y.size() +
                                         nrOfStrands * beadsPerChains[0]);
      this->simplifiedUniverse.z.reserve(this->simplifiedUniverse.z.size() +
                                         nrOfStrands * beadsPerChains[0]);
      this->simplifiedUniverse.x.reserve(this->simplifiedUniverse.x.size() +
                                         nrOfStrands * beadsPerChains[0]);
      this->simplifiedUniverse.bondsFrom.reserve(
        this->simplifiedUniverse.bondsFrom.size() +
        nrOfStrands * beadsPerChains[0]);
      this->simplifiedUniverse.bondsTo.reserve(
        this->simplifiedUniverse.bondsTo.size() +
        nrOfStrands * beadsPerChains[0]);

      //
      std::uniform_real_distribution<double> linkerProbabilityDist =
        std::uniform_real_distribution<double>(0.0, 1.0);
      std::vector<size_t> crosslinkers = this->crosslinkerIdxs;
      std::vector<int> availableCrosslinkerSites =
        initializeWithValue(crosslinkers.size(), crosslinkerFunctionality);
      int nrOfStrandsAdded = 0;
      double conversionPerBond =
        1.0 / (static_cast<double>(crosslinkerFunctionality) *
               static_cast<double>(crosslinkers.size()));
      double currentDegreeOfConversion = this->currentCrosslinkerConversion;

      if (currentDegreeOfConversion != 0.0) {
        throw std::runtime_error(
          "Not implemented yet. Strands may only be linked once.");
      }

      // process all cross-linkers
      for (int i = 0; i < crosslinkers.size(); ++i) {
        const int availableSitesForThisCrosslinker =
          availableCrosslinkerSites[i];
        // loop until this cross-linker is fully connected
        for (int siteToHandle = availableSitesForThisCrosslinker;
             siteToHandle > 0;
             --siteToHandle) {
          if (availableCrosslinkerSites[i] == 0) {
            break;
          }
          if (currentDegreeOfConversion >= crosslinkerConversion) {
            break;
          }
          // decide what type of site this is
          bool isActiveSite =
            linkerProbabilityDist(this->rng) <= crosslinkerConversion;
          bool isDanglingStrand =
            linkerProbabilityDist(this->rng) > crosslinkerConversion;
          // problem: with only the above approach,
          // the desired crosslinker conversion is only reached "probably".
          // that is why we introduce a slightly more sophisticated distinction:
          int remainingStrands = nrOfStrands - nrOfStrandsAdded;
          if (remainingStrands * conversionPerBond * 2 <=
              crosslinkerConversion) {
            isActiveSite = true;
            isDanglingStrand = false;
          }
          if (isActiveSite) {
            int targetIdx = this->findAppropriateLink(
              crosslinkers[i],
              crosslinkers,
              availableCrosslinkerSites,
              std::sqrt((double)beadsPerChains[nrOfStrandsAdded]) *
                this->beadDistance,
              ((double)beadsPerChains[nrOfStrandsAdded]) * this->beadDistance);
            if (targetIdx >= 0 && !isDanglingStrand) {
              double dist =
                this->distanceBetween(crosslinkers[i], crosslinkers[targetIdx]);
              if (dist >= ((double)beadsPerChains[nrOfStrandsAdded]) *
                            this->beadDistance) {
                std::cout << "Got too far off link: " << targetIdx << " for "
                          << i << " has dist " << dist << ""
                          << "" << std::endl;
              }
            }
            if (isDanglingStrand || targetIdx == -1 ||
                (targetIdx == i && availableCrosslinkerSites[i] == 1)) {
              // decision is: dangling
              this->addRandomWalkChainFrom(crosslinkers[i],
                                           beadsPerChains[nrOfStrandsAdded]);
            } else {
              // decision is: connected / network
              // find close enough crosslinker to do the chain to

              this->addRandomWalkChainFromTo(crosslinkers[i],
                                             crosslinkers[targetIdx],
                                             beadsPerChains[nrOfStrandsAdded]);
              currentDegreeOfConversion += conversionPerBond;
            }
            availableCrosslinkerSites[targetIdx] -= 1;
            nrOfStrandsAdded += 1;
            currentDegreeOfConversion += conversionPerBond;

            if (nrOfStrandsAdded >= nrOfStrands &&
                currentDegreeOfConversion < crosslinkerConversion &&
                i + 1 < crosslinkers.size()) {
              throw std::invalid_argument(
                "Not enough strands to satisfy the "
                "requested degree of convergence. Current degree: " +
                std::to_string(currentDegreeOfConversion) + " with " +
                std::to_string(nrOfStrandsAdded) + " strands added. ");
            }
          }
          availableCrosslinkerSites[i] -= 1;
        }
      }

      this->currentCrosslinkerConversion = currentDegreeOfConversion;

      // process the remaining (free) chains
      for (size_t i = nrOfStrandsAdded; i < nrOfStrands; ++i) {
        this->addSolventChains(1, beadsPerChains[i], strandAtomType);
      }
    };

    void addAndLinkStrands(int nrOfStrands,
                           int chainLength,
                           double crosslinkerConversion,
                           int crosslinkerFunctionality = 4,
                           int strandAtomType = 1)
    {
      std::vector<int> chainLengths;
      chainLengths.reserve(nrOfStrands);
      for (int i = 0; i < nrOfStrands; ++i) {
        chainLengths.push_back(chainLength);
      }
      return this->addAndLinkStrands(nrOfStrands,
                                     chainLengths,
                                     crosslinkerConversion,
                                     crosslinkerFunctionality,
                                     strandAtomType);
    };

  private:
    double beadDistance = 0.965;
    double currentCrosslinkerConversion = 0.0;
    int maximumAtomId = 1;
    std::mt19937 rng;
    int crosslinkerType = 0;
    std::uniform_real_distribution<double> distX;
    std::uniform_real_distribution<double> distY;
    std::uniform_real_distribution<double> distZ;
    std::uniform_real_distribution<double> distSelect;
    SimplifiedUniverse simplifiedUniverse;
    std::vector<size_t> crosslinkerIdxs;
    pylimer_tools::entities::Box box;

    /**
     * @brief Do a random walk of certain length to add a chain
     *
     * @param from the starting Atom of the chain
     * @param chainLen the number of additional atoms to add to the chain
     * @param atomType the atom type of the atoms in the chain
     */
    void addRandomWalkChainFrom(size_t idxFrom, int chainLen, int atomType = 1)
    {
      // std::cout << "Doing random walk from" << std::endl;
      std::vector<double> xs;
      xs.reserve(chainLen);
      std::vector<double> ys;
      ys.reserve(chainLen);
      std::vector<double> zs;
      zs.reserve(chainLen);

      std::uniform_real_distribution<double> angleDistribution =
        std::uniform_real_distribution<double>(0, 2 * M_PI);

      double lastX = this->simplifiedUniverse.x[idxFrom];
      double lastY = this->simplifiedUniverse.y[idxFrom];
      double lastZ = this->simplifiedUniverse.z[idxFrom];

      for (int i = 0; i < chainLen; ++i) {
        const double alpha = angleDistribution(this->rng);
        const double beta = angleDistribution(this->rng);
        // coordinate system conversion: confirmation e.g. in
        // https://math.stackexchange.com/a/1385150/738831
        xs.push_back(lastX +
                     this->beadDistance * std::cos(beta) * std::sin(alpha));
        lastX = xs[i];
        ys.push_back(lastY +
                     this->beadDistance * std::cos(beta) * std::cos(alpha));
        lastY = ys[i];
        zs.push_back(lastZ + this->beadDistance * std::sin(beta));
        lastZ = zs[i];
      }

      Positions positions;
      positions.x = xs;
      positions.y = ys;
      positions.z = zs;
      std::vector<size_t> idxs =
        this->addAtomsWithType(chainLen, atomType, positions);
      // initalize some bond specific
      std::vector<size_t> bondsFrom;
      std::vector<size_t> bondsTo;
      bondsFrom.reserve(idxs.size());
      bondsTo.reserve(idxs.size());
      for (size_t idx : idxs) {
        bondsFrom.push_back(this->simplifiedUniverse.ids[idx]);
        bondsTo.push_back(this->simplifiedUniverse.ids[idx]);
      }
      std::vector<int> bondTypes = initializeWithValue(chainLen, 1);
      // make the first bond from the starting bead given
      bondsFrom.insert(bondsFrom.begin(),
                       this->simplifiedUniverse.ids[idxFrom]);
      bondsFrom.pop_back();
      // finally, add the bonds
      this->simplifiedUniverse.bondsFrom.reserve(
        this->simplifiedUniverse.bondsFrom.size() + bondsFrom.size());
      this->simplifiedUniverse.bondsFrom.insert(
        this->simplifiedUniverse.bondsFrom.end(),
        bondsFrom.begin(),
        bondsFrom.end());
      this->simplifiedUniverse.bondsTo.reserve(
        this->simplifiedUniverse.bondsTo.size() + bondsTo.size());
      this->simplifiedUniverse.bondsTo.insert(
        this->simplifiedUniverse.bondsTo.end(), bondsTo.begin(), bondsTo.end());
      // std::cout << "Done random walk from" << std::endl;
    }

    /**
     * @brief Do a random walk of certain length to add a chain from one to
     * another atom
     *
     * @param from the atom to start the random walk from
     * @param to the atom to end the random walk at
     * @param chainLen the number of atoms to add in between from and to
     * @param atomType the type of the atoms to add
     */
    void addRandomWalkChainFromTo(size_t from,
                                  size_t to,
                                  int chainLen,
                                  int atomType = 1)
    {
      // std::cout << "Doing random walk from/to" << std::endl;
      std::vector<double> xs;
      xs.reserve(chainLen);
      std::vector<double> ys;
      ys.reserve(chainLen);
      std::vector<double> zs;
      zs.reserve(chainLen);

      std::uniform_real_distribution<double> angleDistribution =
        std::uniform_real_distribution<double>(0, 2 * M_PI);

      double lastX = this->simplifiedUniverse.x[from];
      double lastY = this->simplifiedUniverse.y[from];
      double lastZ = this->simplifiedUniverse.z[from];

      // support crossing of boundary conditions: find nearest image as target
      // (accept image mismatches)
      double targetX =
        this->box.getLx() < std::sqrt((double)chainLen) * this->beadDistance
          ? this->simplifiedUniverse.x[to]
          : lastX + this->_getDeltaDistance(
                      this->simplifiedUniverse.x[to], lastX, this->box.getLx());
      double targetY =
        this->box.getLy() < std::sqrt((double)chainLen) * this->beadDistance
          ? this->simplifiedUniverse.y[to]
          : lastY + this->_getDeltaDistance(
                      this->simplifiedUniverse.y[to], lastY, this->box.getLy());
      double targetZ =
        this->box.getLz() < std::sqrt((double)chainLen) * this->beadDistance
          ? this->simplifiedUniverse.z[to]
          : lastZ + this->_getDeltaDistance(
                      this->simplifiedUniverse.z[to], lastZ, this->box.getLz());

      for (int i = 0; i < chainLen; ++i) {
        double dx = targetX - lastX;
        double dy = targetY - lastY;
        double dz = targetZ - lastZ;
        // for primary loops, dx, dy & dz are zero, intially.
        // therewith, alpha will be NaN
        double remainingDistance = std::sqrt(dx * dx + dy * dy + dz * dz);
        // alpha = theta in Wikipedia
        double idealAlpha =
          std::acos(std::clamp(dz / remainingDistance, -1.0, 1.0));
        // beta = phi in Wikipedia
        double idealBeta = dx == 0.0 ? (M_PI * 0.5) : (std::atan2(dy, dx));
        double bondLenToUse = this->beadDistance;
        double idealWeight = 0.0;
        double bondsRemaining = ((chainLen - i) + 1);
        if (((remainingDistance) / (bondsRemaining)) > this->beadDistance) {
          // need to constrain, cannot use random alpha & beta
          // TODO: find some a bit more sophisticated probability adjustment (or
          // simply use constraints for probability)
          idealWeight = 1.0;
          bondLenToUse = remainingDistance / (bondsRemaining);
          if (bondLenToUse > 2 * this->beadDistance) {
            std::cout << "Using bond length: " << bondLenToUse << " for "
                      << bondsRemaining << " remaining bonds between " << lastX
                      << ", " << lastY << ", " << lastZ
                      << " to target: " << targetX << ", " << targetY << ", "
                      << targetZ << " with length " << remainingDistance
                      << " at i = " << i << " of " << chainLen << std::endl;
          }
          // std::min(((double)i) / ((double)chainLen) +
          //              (remainingDistance / (chainLen - i + 1)),
          //          1.0);
        }

        double alpha = (1.0 - idealWeight) * angleDistribution(this->rng) +
                       idealWeight * idealAlpha;
        // happens e.g. for primary loops
        if (isnan(alpha)) {
          // std::cout << "Got nan for alpha with idealAlpha = " << idealAlpha
          //           << ", weight = " << idealWeight << ", dx = " << dx
          //           << ", dy = " << dy << ", dz = " << dz << " at i = " << i
          //           << std::endl;
          alpha = isnan(idealAlpha) ? angleDistribution(this->rng) : idealAlpha;
        };
        double beta = (1.0 - idealWeight) * angleDistribution(this->rng) +
                      idealWeight * idealBeta;
        if (isnan(beta)) {
          // std::cout << "Got nan for beta with idealBeta = " << idealBeta
          //           << ", weight = " << idealWeight << ", dx = " << dx
          //           << ", dy = " << dy << ", dz = " << dz << " at i = " << i
          //           << std::endl;

          beta = isnan(idealBeta) ? angleDistribution(this->rng) : idealBeta;
        }
        // std::cout << "Using ideal weight " << idealWeight << " at " << i
        //           << ", remaining d: " << remainingDistance << " with alpha "
        //           << alpha << ", ideal " << idealAlpha << ", beta " << beta
        //           <<
        //           ", ideal " << idealBeta << std::endl;
        // coordinate system conversion: confirmation e.g. in
        // https://math.stackexchange.com/a/1385150/738831 or
        // https://en.wikipedia.org/wiki/Spherical_coordinate_system
        xs.push_back(lastX + bondLenToUse * std::cos(beta) * std::sin(alpha));
        lastX = xs[i];
        ys.push_back(lastY + bondLenToUse * std::sin(beta) * std::sin(alpha));
        lastY = ys[i];
        zs.push_back(lastZ + bondLenToUse * std::cos(alpha));
        lastZ = zs[i];
        assert(!isnan(lastX) && !isnan(lastY) && !isnan(lastZ));
      }

      // std::cout << "Made chain with final " << lastX << ", " << lastY << ", "
      //           << lastZ << " to target: " << targetX << ", " << targetY <<
      //           ",
      //           "
      //           << targetZ << " with length "
      //           << this->getDistance(lastX, lastY, lastZ, targetX, targetY,
      //                                targetZ)
      //           << std::endl;

      Positions positions;
      positions.x = xs;
      positions.y = ys;
      positions.z = zs;
      std::vector<size_t> idxs =
        this->addAtomsWithType(chainLen, atomType, positions);
      // initalize some bond specific
      std::vector<size_t> bondsFrom;
      std::vector<size_t> bondsTo;
      bondsFrom.reserve(idxs.size());
      bondsTo.reserve(idxs.size());
      for (size_t idx : idxs) {
        bondsFrom.push_back(this->simplifiedUniverse.ids[idx]);
        bondsTo.push_back(this->simplifiedUniverse.ids[idx]);
      }
      std::vector<int> bondTypes = initializeWithValue(chainLen, 1);
      // make the first bond from the starting bead given
      bondsFrom.insert(bondsFrom.begin(), this->simplifiedUniverse.ids[from]);
      // and the last bond further to the end of the chain
      bondsTo.insert(bondsTo.end(), this->simplifiedUniverse.ids[to]);
      // finally, actually add the bonds
      // finally, add the bonds
      this->simplifiedUniverse.bondsFrom.reserve(
        this->simplifiedUniverse.bondsFrom.size() + bondsFrom.size());
      this->simplifiedUniverse.bondsFrom.insert(
        this->simplifiedUniverse.bondsFrom.end(),
        bondsFrom.begin(),
        bondsFrom.end());
      this->simplifiedUniverse.bondsTo.reserve(
        this->simplifiedUniverse.bondsTo.size() + bondsTo.size());
      this->simplifiedUniverse.bondsTo.insert(
        this->simplifiedUniverse.bondsTo.end(), bondsTo.begin(), bondsTo.end());
    }

    /**
     * @brief Add atoms (incl. type, id etc.) with given positions to the
     * universe
     *
     * @param nrOfAtomsToAdd the nr. of atoms to add to the universe
     * @param atomType the type of the atoms to add
     * @return std::vector<size_t> the ids of the inserted atoms
     */
    std::vector<size_t> addAtomsWithType(int nrOfAtomsToAdd,
                                         int atomType,
                                         Positions randomPos)
    {
      this->simplifiedUniverse.ids.reserve(this->simplifiedUniverse.ids.size() +
                                           nrOfAtomsToAdd);
      this->simplifiedUniverse.types.reserve(
        this->simplifiedUniverse.types.size() + nrOfAtomsToAdd);
      this->simplifiedUniverse.x.reserve(this->simplifiedUniverse.x.size() +
                                         nrOfAtomsToAdd);
      this->simplifiedUniverse.y.reserve(this->simplifiedUniverse.y.size() +
                                         nrOfAtomsToAdd);
      this->simplifiedUniverse.z.reserve(this->simplifiedUniverse.z.size() +
                                         nrOfAtomsToAdd);

      int baseId = this->maximumAtomId + 1;
      std::vector<size_t> indicesAdded;
      indicesAdded.reserve(nrOfAtomsToAdd);
      size_t indexToStartWith = this->simplifiedUniverse.ids.size();

      for (size_t i = 0; i < nrOfAtomsToAdd; ++i) {
        this->simplifiedUniverse.ids.push_back(i + baseId);
        this->simplifiedUniverse.types.push_back(atomType);
        indicesAdded.push_back(indexToStartWith + i);
      }

      this->simplifiedUniverse.x.insert(this->simplifiedUniverse.x.end(),
                                        randomPos.x.begin(),
                                        randomPos.x.end());
      this->simplifiedUniverse.y.insert(this->simplifiedUniverse.y.end(),
                                        randomPos.y.begin(),
                                        randomPos.y.end());
      this->simplifiedUniverse.z.insert(this->simplifiedUniverse.z.end(),
                                        randomPos.z.begin(),
                                        randomPos.z.end());

      this->maximumAtomId += nrOfAtomsToAdd + 1;
      return indicesAdded;
    }

    /**
     * @brief Add atoms (incl. random positions, id etc.) to the universe
     *
     * @param nrOfAtomsToAdd the nr. of atoms to add to the universe
     * @param atomType the type of the atoms to add
     * @return std::vector<size_t> the ids of the inserted atoms
     */
    std::vector<size_t> addAtomsWithType(int nrOfAtomsToAdd, int atomType)
    {
      Positions randomPos = this->generateRandomPositions(nrOfAtomsToAdd);
      return this->addAtomsWithType(nrOfAtomsToAdd, atomType, randomPos);
    }

    /**
     * @brief Generate positions randomly
     *
     * @param nSamples the number of positions to generate
     * @return Positions
     */
    Positions generateRandomPositions(int nSamples)
    {
      if (nSamples < 1000) {
        return this->generateRandomBluePositions(nSamples);
      } else {
        return this->generateRandomWhitePositions(nSamples);
      }
    }

    /**
     * @brief Generate positions randomly (can lead to clustering)
     *
     * @param nSamples the number of positions to generate
     * @return Positions
     */
    Positions generateRandomWhitePositions(int nSamples)
    {
      std::vector<double> xs;
      std::vector<double> ys;
      std::vector<double> zs;

      for (size_t i = 0; i < nSamples; ++i) {
        double x = this->distX(this->rng);
        double y = this->distY(this->rng);
        double z = this->distZ(this->rng);

        xs.push_back(x);
        ys.push_back(y);
        zs.push_back(z);
      }

      Positions result;
      result.x = xs;
      result.y = ys;
      result.z = zs;
      return result;
    }

    /**
     * @brief Generate positions randomly according to blue noise type sampling
     *
     * @param nSamples the number of positions to generate
     * @return Positions
     */
    Positions generateRandomBluePositions(int nSamples)
    {

      std::vector<double> xs;
      std::vector<double> ys;
      std::vector<double> zs;

      // blue noise
      // inspiration:
      // https://github.com/Atrix256/RandomCode/blob/master/Mitchell/Source.cpp
      for (size_t i = 0; i < nSamples; ++i) {
        size_t numCandidates =
          std::min((size_t)(i * 1 + 1),
                   (size_t)500); // decrease the multiplier to speed things up
        double bestDistance = 0.0;
        double bestCandidateX = 0.0;
        double bestCandidateY = 0.0;
        double bestCandidateZ = 0.0;

        for (size_t j = 0; j < numCandidates; ++j) {
          double x = this->distX(this->rng);
          double y = this->distY(this->rng);
          double z = this->distZ(this->rng);

          double minDistance = std::numeric_limits<double>::max();
          for (size_t k = 0; k < xs.size(); ++k) {
            double dist = this->getDistance(x, y, z, xs[k], ys[k], zs[k]);
            if (dist < minDistance) {
              minDistance = dist;
            }
          }

          if (minDistance > bestDistance) {
            bestDistance = minDistance;

            bestCandidateX = x;
            bestCandidateY = y;
            bestCandidateZ = z;
          }
        }

        xs.push_back(bestCandidateX);
        ys.push_back(bestCandidateY);
        zs.push_back(bestCandidateZ);
      }

      Positions result;
      result.x = xs;
      result.y = ys;
      result.z = zs;
      return result;
    }

    /**
     * @brief find an Atom in a collection with an objective distance
     *
     * TODO: check probabilities to not only select the very best.
     *
     * @param from the Atom to start the distance from
     * @param possiblePartners the Atoms that could be the target
     * @param desiredDistance the distance to target if possible
     * @param maxDistance the maximum distance to accept random matches from
     * @return int the index in possiblePartners that matches best
     */
    int findAppropriateLink(size_t from,
                            std::vector<size_t> possiblePartners,
                            std::vector<int> availablePartnerSites,
                            const double desiredDistance,
                            const double maxDistance)
    {
      if (possiblePartners.size() == 0) {
        throw std::invalid_argument("Cannot find a partner in none.");
      }
      // double bestDistance = std::numeric_limits<double>::max();
      // int bestMatch = -1;
      std::vector<int> suitableMatches;
      for (int i = 0; i < possiblePartners.size(); ++i) {
        if (availablePartnerSites[i] < 1) {
          continue;
        }
        size_t partner = possiblePartners[i];
        double distBetween = this->distanceBetween(partner, from);
        if (distBetween < maxDistance) {
          suitableMatches.push_back(i);
          // double currDist = std::fabs(distBetween - desiredDistance);
          // if (currDist < bestDistance) {
          //   bestDistance = currDist;
          //   bestMatch = i;
          // }
        }
      }

      std::uniform_int_distribution<int> idxDist(0, suitableMatches.size() - 1);
      return suitableMatches.size() == 0 ? -1
                                         : suitableMatches[idxDist(this->rng)];
    }

    double distanceBetween(size_t i, size_t j)
    {
      return this->getDistance(this->simplifiedUniverse.x[i],
                               this->simplifiedUniverse.y[i],
                               this->simplifiedUniverse.z[i],
                               this->simplifiedUniverse.x[j],
                               this->simplifiedUniverse.y[j],
                               this->simplifiedUniverse.z[j]);
    }

    double getDistance(double x1,
                       double y1,
                       double z1,
                       double x2,
                       double y2,
                       double z2)
    {
      double dx = this->_getDeltaDistance(x1, x2, this->box.getLx());
      double dy = this->_getDeltaDistance(y1, y2, this->box.getLy());
      double dz = this->_getDeltaDistance(z1, z2, this->box.getLz());
      return std::sqrt(dx * dx + dy * dy + dz * dz);
    }

    double _getDeltaDistance(double c1, double c2, double boxL) const
    {
      double delta = c1 - c2;
      while (delta > 0.5 * boxL) {
        delta -= boxL;
      }
      while (delta < -0.5 * boxL) {
        delta += boxL;
      }

      return delta;
    }
  };
} // namespace utils
} // namespace pylimer_tools

#endif
