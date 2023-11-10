#ifndef DLPLAN_INCLUDE_DLPLAN_UTILS_DYNAMIC_BITSET_H
#define DLPLAN_INCLUDE_DLPLAN_UTILS_DYNAMIC_BITSET_H

#include "hash.h"

#include <boost/serialization/vector.hpp>

#include <cassert>
#include <limits>
#include <vector>


namespace dlplan::utils {
template<typename Block>
class DynamicBitset;
}


namespace boost::serialization {
    class access;

    template <typename Archive, typename Block>
    void serialize(Archive& ar, dlplan::utils::DynamicBitset<Block>& t, const unsigned int version);
}


/*
  Poor man's version of boost::dynamic_bitset, mostly copied from there.
*/
namespace dlplan::utils {

template<typename Block = unsigned int>
class DynamicBitset {
    static_assert(
        !std::numeric_limits<Block>::is_signed,
        "Block type must be unsigned");

    std::vector<Block> blocks;
    std::size_t num_bits;

    static const Block zeros;
    static const Block ones;

    static const int bits_per_block = std::numeric_limits<Block>::digits;

    static int compute_num_blocks(std::size_t num_bits) {
        return num_bits / bits_per_block +
               static_cast<int>(num_bits % bits_per_block != 0);
    }

    static std::size_t block_index(std::size_t pos) {
        return pos / bits_per_block;
    }

    static std::size_t bit_index(std::size_t pos) {
        return pos % bits_per_block;
    }

    static Block bit_mask(std::size_t pos) {
        return Block(1) << bit_index(pos);
    }

    int count_bits_in_last_block() const {
        return bit_index(num_bits);
    }

    void zero_unused_bits() {
        const int bits_in_last_block = count_bits_in_last_block();

        if (bits_in_last_block != 0) {
            assert(!blocks.empty());
            blocks.back() &= ~(ones << bits_in_last_block);
        }
    }

    /// @brief Constructor for serialization.
    DynamicBitset() : blocks(std::vector<Block>()), num_bits(0) { }

    friend class boost::serialization::access;
    template<typename Archive, typename Block_>
    friend void boost::serialization::serialize(Archive& ar, DynamicBitset<Block_>& t, const unsigned int version);

public:
    explicit DynamicBitset(std::size_t num_bits)
        : blocks(compute_num_blocks(num_bits), zeros),
          num_bits(num_bits) {
    }

    std::size_t size() const {
        return num_bits;
    }

    /*
      Count the number of set bits.

      The computation could be made faster by using a more sophisticated
      algorithm (see https://en.wikipedia.org/wiki/Hamming_weight).
    */
    int count() const {
        int result = 0;
        for (std::size_t pos = 0; pos < num_bits; ++pos) {
            result += static_cast<int>(test(pos));
        }
        return result;
    }

    bool none() const {
        for (std::size_t i = 0; i < blocks.size(); ++i) {
            if (blocks[i]) return false;
        }
        return true;
    }

    void set() {
        std::fill(blocks.begin(), blocks.end(), ones);
        zero_unused_bits();
    }

    void reset() {
        std::fill(blocks.begin(), blocks.end(), zeros);
    }

    void set(std::size_t pos) {
        assert(pos < num_bits);
        blocks[block_index(pos)] |= bit_mask(pos);
    }

    void reset(std::size_t pos) {
        assert(pos < num_bits);
        blocks[block_index(pos)] &= ~bit_mask(pos);
    }

    bool test(std::size_t pos) const {
        assert(pos < num_bits);
        return (blocks[block_index(pos)] & bit_mask(pos)) != 0;
    }

    bool operator[](std::size_t pos) const {
        return test(pos);
    }

    bool operator==(const DynamicBitset& other) const {
        if (this != &other) {
            return (blocks == other.blocks) && (num_bits == other.num_bits);
        }
        return true;
    }

    bool operator!=(const DynamicBitset& other) const {
        return !(*this == other);
    }

    DynamicBitset& operator&=(const DynamicBitset& other) {
        assert(size() == other.size());
        for (std::size_t i = 0; i < blocks.size(); ++i) {
            blocks[i] &= other.blocks[i];
        }
        return *this;
    }

    DynamicBitset& operator|=(const DynamicBitset& other) {
        assert(size() == other.size());
        for (std::size_t i = 0; i < blocks.size(); ++i) {
            blocks[i] |= other.blocks[i];
        }
        return *this;
    }

    DynamicBitset& operator-=(const DynamicBitset& other) {
        assert(size() == other.size());
        for (std::size_t i = 0; i < blocks.size(); ++i) {
            blocks[i] = blocks[i] & ~other.blocks[i];
        }
        return *this;
    }

    DynamicBitset& operator~() {
        for (std::size_t i = 0; i < blocks.size(); ++i) {
            blocks[i] = ~blocks[i];
        }
        zero_unused_bits();
        return *this;
    }

    bool intersects(const DynamicBitset &other) const {
        assert(size() == other.size());
        for (std::size_t i = 0; i < blocks.size(); ++i) {
            if (blocks[i] & other.blocks[i])
                return true;
        }
        return false;
    }

    bool is_subset_of(const DynamicBitset &other) const {
        assert(size() == other.size());
        for (std::size_t i = 0; i < blocks.size(); ++i) {
            if (blocks[i] & ~other.blocks[i])
                return false;
        }
        return true;
    }

    std::size_t hash() const {
        return dlplan::utils::hash<std::vector<Block>>()(blocks);
    }
};

template<typename Block>
const Block DynamicBitset<Block>::zeros = Block(0);

template<typename Block>
const Block DynamicBitset<Block>::ones = ~DynamicBitset<Block>::zeros;
}

namespace boost::serialization {

template<typename Archive, typename Block>
void serialize(Archive& ar, dlplan::utils::DynamicBitset<Block>& t, const unsigned int /* version */) {
    ar & t.blocks;
    ar & t.num_bits;
}

}

/*
This source file was derived from the boost::dynamic_bitset library
version 1.54. Original copyright statement and license for this
original source follow.

Copyright (c) 2001-2002 Chuck Allison and Jeremy Siek
Copyright (c) 2003-2006, 2008 Gennaro Prota

Distributed under the Boost Software License, Version 1.0.

Boost Software License - Version 1.0 - August 17th, 2003

Permission is hereby granted, free of charge, to any person or organization
obtaining a copy of the software and accompanying documentation covered by
this license (the "Software") to use, reproduce, display, distribute,
execute, and transmit the Software, and to prepare derivative works of the
Software, and to permit third-parties to whom the Software is furnished to
do so, all subject to the following:

The copyright notices in the Software and this entire statement, including
the above license grant, this restriction and the following disclaimer,
must be included in all copies of the Software, in whole or in part, and
all derivative works of the Software, unless such copies or derivative
works are solely in the form of machine-executable object code generated by
a source language processor.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT
SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE
FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
*/

#endif
