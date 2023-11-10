#ifndef DLPLAN_SRC_CORE_ELEMENTS_ROLES_TRANSITIVE_REFLEXIVE_CLOSURE_H_
#define DLPLAN_SRC_CORE_ELEMENTS_ROLES_TRANSITIVE_REFLEXIVE_CLOSURE_H_

#include "../utils.h"
#include "../../../../include/dlplan/core.h"

#include <boost/archive/text_oarchive.hpp>
#include <boost/archive/text_iarchive.hpp>
#include <boost/serialization/export.hpp>
#include <boost/serialization/base_object.hpp>
#include <boost/serialization/shared_ptr.hpp>

#include <sstream>
#include <memory>

using namespace std::string_literals;


namespace dlplan::core {
class TransitiveReflexiveClosureRole;
}


namespace boost::serialization {
    template<typename Archive>
    void serialize(Archive& ar, dlplan::core::TransitiveReflexiveClosureRole& t, const unsigned int version);
    template<class Archive>
    void save_construct_data(Archive& ar, const dlplan::core::TransitiveReflexiveClosureRole* t, const unsigned int version);
    template<class Archive>
    void load_construct_data(Archive& ar, dlplan::core::TransitiveReflexiveClosureRole* t, const unsigned int version);
}


namespace dlplan::core {
class TransitiveReflexiveClosureRole : public Role {
private:
    void compute_result(const RoleDenotation& denot, int num_objects, RoleDenotation& result) const {
        result = denot;
        bool changed = false;
        do {
            RoleDenotation tmp_result = result;
            PairsOfObjectIndices pairs = tmp_result.to_vector();
            for (const auto& pair_1 : pairs) {
                for (const auto& pair_2 : pairs) {
                    if (pair_1.second == pair_2.first) {
                        result.insert(std::make_pair(pair_1.first, pair_2.second));
                    }
                }
            }
            changed = (result.size() != tmp_result.size());
        } while (changed);
        // add reflexive part
        for (int i = 0; i < num_objects; ++i) {
            result.insert(std::make_pair(i, i));
        }
    }

    RoleDenotation evaluate_impl(const State& state, DenotationsCaches& caches) const override {
        RoleDenotation denotation(state.get_instance_info()->get_objects().size());
        compute_result(
            *m_role->evaluate(state, caches),
            state.get_instance_info()->get_objects().size(),
            denotation);
        return denotation;
    }

    RoleDenotations evaluate_impl(const States& states, DenotationsCaches& caches) const override {
        RoleDenotations denotations;
        denotations.reserve(states.size());
        auto role_denotations = m_role->evaluate(states, caches);
        for (size_t i = 0; i < states.size(); ++i) {
            RoleDenotation denotation(states[i].get_instance_info()->get_objects().size());
            compute_result(
                *(*role_denotations)[i],
                states[i].get_instance_info()->get_objects().size(),
                denotation);
            denotations.push_back(caches.role_denotation_cache.insert_denotation(std::move(denotation)));
        }
       return denotations;
    }

    template<typename Archive>
    friend void boost::serialization::serialize(Archive& ar, TransitiveReflexiveClosureRole& t, const unsigned int version);
    template<class Archive>
    friend void boost::serialization::save_construct_data(Archive& ar, const TransitiveReflexiveClosureRole* t, const unsigned int version);
    template<class Archive>
    friend void boost::serialization::load_construct_data(Archive& ar, TransitiveReflexiveClosureRole* t, const unsigned int version);

protected:
    const std::shared_ptr<const Role> m_role;

public:
    TransitiveReflexiveClosureRole(std::shared_ptr<VocabularyInfo> vocabulary_info, ElementIndex index, std::shared_ptr<const Role> role)
    : Role(vocabulary_info, index, role->is_static()), m_role(role) {
        if (!role) {
            throw std::runtime_error("TransitiveReflexiveClosureRole::TransitiveReflexiveClosureRole - child is a nullptr.");
        }
    }

    RoleDenotation evaluate(const State& state) const override {
        int num_objects = state.get_instance_info()->get_objects().size();
        RoleDenotation denotation(num_objects);
        compute_result(
            m_role->evaluate(state),
            num_objects,
            denotation);
        return denotation;
    }

    int compute_complexity() const override {
        return m_role->compute_complexity() + 1;
    }

    void compute_repr(std::stringstream& out) const override {
        out << "r_transitive_reflexive_closure" << "(";
        m_role->compute_repr(out);
        out << ")";
    }

    int compute_evaluate_time_score() const override {
        return m_role->compute_evaluate_time_score() + SCORE_QUBIC;
    }
};

}


namespace boost::serialization {
template<typename Archive>
void serialize(Archive& /* ar */ , dlplan::core::TransitiveReflexiveClosureRole& t, const unsigned int /* version */ )
{
    boost::serialization::base_object<dlplan::core::Role>(t);
}

template<class Archive>
void save_construct_data(Archive & ar, const dlplan::core::TransitiveReflexiveClosureRole* t, const unsigned int /* version */ )
{
    ar << t->m_vocabulary_info;
    ar << t->m_index;
    ar << t->m_role;
}

template<class Archive>
void load_construct_data(Archive & ar, dlplan::core::TransitiveReflexiveClosureRole* t, const unsigned int /* version */ )
{
    std::shared_ptr<dlplan::core::VocabularyInfo> vocabulary;
    int index;
    std::shared_ptr<const dlplan::core::Role> role;
    ar >> vocabulary;
    ar >> index;
    ar >> role;
    ::new(t)dlplan::core::TransitiveReflexiveClosureRole(vocabulary, index, role);
}

}

BOOST_CLASS_EXPORT_GUID(dlplan::core::TransitiveReflexiveClosureRole, "dlplan::core::TransitiveReflexiveClosureRole")

#endif
