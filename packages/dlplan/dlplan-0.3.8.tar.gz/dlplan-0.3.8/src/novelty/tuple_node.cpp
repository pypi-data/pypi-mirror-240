#include "../../include/dlplan/novelty.h"

#include "../utils/logging.h"

#include <boost/archive/text_oarchive.hpp>
#include <boost/archive/text_iarchive.hpp>
#include <boost/serialization/vector.hpp>

#include <sstream>

using namespace dlplan::state_space;


namespace dlplan::novelty {

TupleNode::TupleNode()
    : m_index(-1),
      m_tuple_index(-1),
      m_state_indices(state_space::StateIndices()),
      m_predecessors(TupleNodeIndices()),
      m_successors(TupleNodeIndices()) {
}

TupleNode::TupleNode(TupleNodeIndex index, TupleIndex tuple_index, const StateIndices& state_indices)
    : m_index(index), m_tuple_index(tuple_index), m_state_indices(state_indices) { }

TupleNode::TupleNode(TupleNodeIndex index, TupleIndex tuple_index, StateIndices&& state_indices)
    : m_index(index), m_tuple_index(tuple_index), m_state_indices(std::move(state_indices)) { }

TupleNode::TupleNode(const TupleNode& other) = default;

TupleNode& TupleNode::operator=(const TupleNode& other) = default;

TupleNode::TupleNode(TupleNode&& other) = default;

TupleNode& TupleNode::operator=(TupleNode&& other) = default;

TupleNode::~TupleNode() = default;

void TupleNode::add_predecessor(TupleIndex tuple_index) {
    m_predecessors.push_back(tuple_index);
}

void TupleNode::add_successor(TupleIndex tuple_index) {
    m_successors.push_back(tuple_index);
}

std::string TupleNode::compute_repr() const {
    std::stringstream ss;
    state_space::StateIndices sorted_state_indices(m_state_indices.begin(), m_state_indices.end());
    std::sort(sorted_state_indices.begin(), sorted_state_indices.end());
    TupleIndices sorted_predecessors(m_predecessors.begin(), m_predecessors.end());
    std::sort(sorted_predecessors.begin(), sorted_predecessors.end());
    TupleIndices sorted_successors(m_successors.begin(), m_successors.end());
    std::sort(sorted_successors.begin(), sorted_successors.end());
    ss << "TupleNode("
       << "index=" << m_index << ", "
       << "tuple_index=" << m_tuple_index << ", "
       << "state_indices=" << sorted_state_indices << ", "
       << "predecessors=" << sorted_predecessors << ", "
       << "successors=" << sorted_successors
       << ")";
    return ss.str();
}

std::ostream& operator<<(std::ostream& os, const TupleNode& tuple_node) {
    os << tuple_node.compute_repr();
    return os;
}

std::string TupleNode::str() const {
    std::stringstream result;
    result << "(" << m_tuple_index << ", " << m_state_indices << ")";
    return result.str();
}

TupleNodeIndex TupleNode::get_index() const {
    return m_index;
}

TupleIndex TupleNode::get_tuple_index() const {
    return m_tuple_index;
}

const StateIndices& TupleNode::get_state_indices() const {
    return m_state_indices;
}

const TupleIndices& TupleNode::get_predecessors() const {
    return m_predecessors;
}

const TupleIndices& TupleNode::get_successors() const {
    return m_successors;
}

}


namespace boost::serialization {
template<typename Archive>
void serialize(Archive& ar, dlplan::novelty::TupleNode& t, const unsigned int /* version */ )
{
    ar & t.m_index;
    ar & t.m_tuple_index;
    ar & t.m_state_indices;
    ar & t.m_predecessors;
    ar & t.m_successors;
}

template void serialize(boost::archive::text_iarchive& ar,
    dlplan::novelty::TupleNode& t, const unsigned int version);
template void serialize(boost::archive::text_oarchive& ar,
    dlplan::novelty::TupleNode& t, const unsigned int version);
}