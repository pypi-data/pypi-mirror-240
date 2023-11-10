#include "../../include/dlplan/policy.h"

#include "condition.h"
#include "effect.h"
#include "../../include/dlplan/core.h"

#include <boost/archive/text_oarchive.hpp>
#include <boost/archive/text_iarchive.hpp>
#include <boost/serialization/set.hpp>
#include <boost/serialization/shared_ptr.hpp>

#include <algorithm>
#include <sstream>


namespace dlplan::policy {

Policy::Policy()
    : m_booleans(Booleans()),
      m_numericals(Numericals()),
      m_rules(Rules()),
      m_index(-1) { }

Policy::Policy(const Rules& rules, PolicyIndex index)
    : m_rules(rules), m_index(index) {
    // Retrieve boolean and numericals from the rules.
    for (const auto& rule : m_rules) {
        for (const auto& condition : rule->get_conditions()) {
            const auto boolean = condition->get_boolean();
            if (boolean) {
                m_booleans.insert(boolean);
            }
            const auto numerical = condition->get_numerical();
            if (numerical) {
                m_numericals.insert(numerical);
            }
        }
        for (const auto& effect : rule->get_effects()) {
            const auto boolean = effect->get_boolean();
            if (boolean) {
                m_booleans.insert(boolean);
            }
            const auto numerical = effect->get_numerical();
            if (numerical) {
                m_numericals.insert(numerical);
            }
        }
    }
}

Policy::Policy(const Policy& other) = default;

Policy& Policy::operator=(const Policy& other) = default;

Policy::Policy(Policy&& other) = default;

Policy& Policy::operator=(Policy&& other) = default;

Policy::~Policy() = default;

std::shared_ptr<const Rule> Policy::evaluate(const core::State& source_state, const core::State& target_state) const {
    for (const auto& r : m_rules) {
        if (r->evaluate_conditions(source_state) && r->evaluate_effects(source_state, target_state)) {
            return r;
        }
    }
    return nullptr;
}

std::shared_ptr<const Rule> Policy::evaluate(const core::State& source_state, const core::State& target_state, core::DenotationsCaches& caches) const {
    for (const auto& r : m_rules) {
        if (r->evaluate_conditions(source_state, caches) && r->evaluate_effects(source_state, target_state, caches)) {
            return r;
        }
    }
    return nullptr;
}

std::vector<std::shared_ptr<const Rule>> Policy::evaluate_conditions(const core::State& source_state) const {
    std::vector<std::shared_ptr<const Rule>> result;
    for (const auto& r : m_rules) {
        if (r->evaluate_conditions(source_state)) {
            result.push_back(r);
        }
    }
    return result;
}

std::vector<std::shared_ptr<const Rule>> Policy::evaluate_conditions(const core::State& source_state, core::DenotationsCaches& caches) const {
    std::vector<std::shared_ptr<const Rule>> result;
    for (const auto& r : m_rules) {
        if (r->evaluate_conditions(source_state, caches)) {
            result.push_back(r);
        }
    }
    return result;
}

std::shared_ptr<const Rule> Policy::evaluate_effects(const core::State& source_state, const core::State& target_state, const std::vector<std::shared_ptr<const Rule>>& rules) const {
    for (const auto& r : rules) {
        if (r->evaluate_effects(source_state, target_state)) {
            return r;
        }
    }
    return nullptr;
}

std::shared_ptr<const Rule> Policy::evaluate_effects(const core::State& source_state, const core::State& target_state, const std::vector<std::shared_ptr<const Rule>>& rules, core::DenotationsCaches& caches) const {
    for (const auto& r : rules) {
        if (r->evaluate_effects(source_state, target_state, caches)) {
            return r;
        }
    }
    return nullptr;
}


std::string Policy::compute_repr() const {
    // Canonical representation
    std::stringstream ss;
    ss << "(:policy\n";
    std::vector<std::shared_ptr<const Rule>> sorted_rules(m_rules.begin(), m_rules.end());
    std::sort(sorted_rules.begin(), sorted_rules.end(), [](const auto& r1, const auto& r2){ return r1->compute_repr() < r2->compute_repr(); });
    for (const auto& r : sorted_rules) {
        ss << r->compute_repr() << "\n";
    }
    ss << ")";
    return ss.str();
}

std::string Policy::str() const {
    std::stringstream ss;
    ss << "(:policy\n";
    ss << "(:booleans ";
    for (const auto& boolean : m_booleans) {
        ss << "(" << boolean->get_key() << " \"" << boolean->get_boolean()->compute_repr() << "\")";
        if (boolean != *m_booleans.rbegin()) ss << " ";
    }
    ss << ")\n";
    ss << "(:numericals ";
    for (const auto& numerical : m_numericals) {
        ss << "(" << numerical->get_key() << " \"" << numerical->get_numerical()->compute_repr() << "\")";
        if (numerical != *m_numericals.rbegin()) ss << " ";
    }
    ss << ")\n";
    for (const auto& rule : m_rules) {
        ss << rule->str() << "\n";
    }
    ss << ")";
    return ss.str();
}

int Policy::compute_evaluate_time_score() const {
    int score = 0;
    for (const auto& rule : m_rules) {
        score += rule->compute_evaluate_time_score();
    }
    return score;
}

PolicyIndex Policy::get_index() const {
    return m_index;
}

const Booleans& Policy::get_booleans() const {
    return m_booleans;
}

const Numericals& Policy::get_numericals() const {
    return m_numericals;
}

const Rules& Policy::get_rules() const {
    return m_rules;
}

}


namespace boost::serialization {
template<typename Archive>
void serialize(Archive& ar, dlplan::policy::Policy& t, const unsigned int /* version */ )
{
    ar & t.m_index;
    ar & t.m_booleans;
    ar & t.m_numericals;
    ar & t.m_rules;
}

template void serialize(boost::archive::text_iarchive& ar,
    dlplan::policy::Policy& t, const unsigned int version);
template void serialize(boost::archive::text_oarchive& ar,
    dlplan::policy::Policy& t, const unsigned int version);
}