"""Other event implementations.

"""

from __future__ import annotations

import random
from typing import Any, Optional

from neighborly.components.business import (
    Business,
    JobRole,
    Occupation,
    OpenForBusiness,
    OpenToPublic,
    PendingOpening,
    Unemployed,
)
from neighborly.components.character import Character, LifeStage, Pregnant, Sex
from neighborly.components.relationship import Relationship, Relationships
from neighborly.components.residence import Resident, ResidentialUnit, Vacant
from neighborly.components.settlement import District
from neighborly.datetime import SimDate
from neighborly.ecs import Active, GameObject
from neighborly.events.defaults import ChangeResidenceEvent, DepartSettlement, LeaveJob
from neighborly.helpers.location import add_frequented_location
from neighborly.helpers.relationship import (
    get_relationship,
    get_relationships_with_traits,
)
from neighborly.helpers.stats import get_stat
from neighborly.helpers.traits import add_trait, has_trait, remove_trait
from neighborly.life_event import EventRole, LifeEvent, event_consideration
from neighborly.loaders import register_life_event_type
from neighborly.simulation import Simulation

# class MeetSomeoneNew(LifeEvent):
#     """A character will attempt to initiate a new social relationship with someone new.

#     Notes
#     -----
#     This system uses a character's sociability stat score to determine the probability
#     of them introducing themselves to someone else. The goal is for characters with
#     higher sociability scores to form more relationships over the course of their lives.
#     """

#     def __init__(
#         self,
#         initiator: GameObject,
#         other: GameObject,
#     ) -> None:
#         super().__init__(
#             world=initiator.world,
#             roles=(
#                 EventRole("subject", initiator, True),
#                 EventRole("other", other, True),
#             ),
#         )

#     @staticmethod
#     @event_consideration
#     def subject_sociability(event: MeetSomeoneNew) -> float:
#         """Add a consideration for the subject's sociability stat."""
#         return get_stat(event.roles["subject"], "sociability").normalized

#     @staticmethod
#     @event_consideration
#     def other_person_sociability(event: MeetSomeoneNew) -> float:
#         """Add a consideration for the subject's sociability stat."""
#         return get_stat(event.roles["other"], "sociability").normalized

#     @classmethod
#     def instantiate(cls, subject: GameObject, **kwargs: Any) -> LifeEvent | None:
#         candidate_scores: defaultdict[GameObject, int] = defaultdict(int)

#         frequented_locations = subject.get_component(FrequentedLocations)

#         for loc in frequented_locations:
#             for other in loc.get_component(FrequentedBy):
#                 if other != subject and not has_relationship(subject, other):
#                     candidate_scores[other] += 1

#         if candidate_scores:
#             rng = subject.world.resource_manager.get_resource(random.Random)

#             acquaintance = rng.choices(
#                 list(candidate_scores.keys()),
#                 weights=list(candidate_scores.values()),
#                 k=1,
#             )[0]

#             return MeetSomeoneNew(subject, acquaintance)

#         return None

#     def execute(self) -> None:
#         subject = self.roles["subject"]
#         other = self.roles["other"]

#         add_relationship(subject, other)
#         add_relationship(other, subject)

#         overlapping_frequents = len(
#             set(subject.get_component(FrequentedLocations)).intersection(
#                 set(other.get_component(FrequentedLocations))
#             )
#         )

#         get_stat(get_relationship(subject, other), "reputation").base_value += 3
#         get_stat(get_relationship(other, subject), "reputation").base_value += 3

#         get_stat(
#             get_relationship(subject, other),
#             "interaction_score",
#         ).base_value += overlapping_frequents

#         get_stat(
#             get_relationship(other, subject),
#             "interaction_score",
#         ).base_value += overlapping_frequents

#     def __str__(self) -> str:
#         return (
#             f"{self.roles['subject'].name} and "
#             f"{self.roles['other'].name} became acquaintances."
#         )


class StartANewJob(LifeEvent):
    """A character will attempt to find a job."""

    base_probability = 0.5

    def __init__(
        self, subject: GameObject, business: GameObject, job_role: GameObject
    ) -> None:
        super().__init__(
            world=subject.world,
            roles=(
                EventRole("subject", subject, True),
                EventRole("business", business),
                EventRole("job_role", job_role),
            ),
        )

    @staticmethod
    @event_consideration
    def has_job_consideration(event: StartANewJob) -> float:
        """check if the character already has a job."""
        if event.roles["subject"].has_component(Occupation):
            return 0

        return -1

    @staticmethod
    @event_consideration
    def number_children_consideration(event: StartANewJob) -> float:
        """Consider the number of children the character has."""
        subject = event.roles["subject"]
        child_count = len(get_relationships_with_traits(subject, "child"))

        if child_count != 0:
            return min(1.0, child_count / 5.0)

        return -1

    @staticmethod
    @event_consideration
    def boldness_consideration(event: StartANewJob) -> float:
        """Considers the subject's boldness stat."""
        return get_stat(event.roles["subject"], "boldness").normalized

    @staticmethod
    @event_consideration
    def reliability_consideration(event: StartANewJob) -> float:
        """Considers the subjects reliability stat."""
        return get_stat(event.roles["subject"], "reliability").normalized

    @staticmethod
    @event_consideration
    def time_unemployed_consideration(event: StartANewJob) -> float:
        """Calculate consideration score based on the amount of time unemployed."""
        subject = event.roles["subject"]

        if unemployed := subject.try_component(Unemployed):
            current_date = subject.world.resource_manager.get_resource(SimDate)
            months_unemployed = (
                current_date.total_months - unemployed.timestamp.total_months
            )
            return min(1.0, float(months_unemployed) / 6.0)

        return -1

    @staticmethod
    @event_consideration
    def relationship_with_owner(event: StartANewJob) -> float:
        """Considers the subject's reputation with the business' owner."""
        subject = event.roles["subject"]
        business_owner = event.roles["business"].get_component(Business).owner

        if business_owner is not None:
            return get_stat(
                get_relationship(business_owner, subject),
                "reputation",
            ).normalized

        return -1

    def execute(self) -> None:
        character = self.roles["subject"]
        business = self.roles["business"]
        job_role = self.roles["job_role"]

        business_comp = business.get_component(Business)
        current_date = self.world.resource_manager.get_resource(SimDate)

        character.add_component(
            Occupation(
                business=business,
                start_date=current_date,
                job_role=job_role.get_component(JobRole),
            )
        )

        add_frequented_location(character, business)

        if character.has_component(Unemployed):
            character.remove_component(Unemployed)

        # Update boss/employee relationships if needed
        if business_comp.owner is not None:
            add_trait(get_relationship(character, business_comp.owner), "boss")
            add_trait(get_relationship(business_comp.owner, character), "employee")

        # Update employee/employee relationships
        for employee, _ in business_comp.employees.items():
            add_trait(get_relationship(character, employee), "coworker")
            add_trait(get_relationship(employee, character), "coworker")

        business_comp.add_employee(character, job_role.get_component(JobRole))

    @classmethod
    def instantiate(cls, subject: GameObject, **kwargs: Any) -> LifeEvent | None:
        rng = subject.world.resource_manager.get_resource(random.Random)

        active_businesses = subject.world.get_components(
            (Business, OpenForBusiness, Active)
        )

        rng.shuffle(active_businesses)

        for _, (business, _, _) in active_businesses:
            open_positions = business.get_open_positions()

            for job_role in open_positions:
                if job_role.check_requirements(subject):
                    return StartANewJob(
                        subject=subject,
                        business=business.gameobject,
                        job_role=job_role.gameobject,
                    )

        return None

    def __str__(self) -> str:
        subject = self.roles["subject"]
        business = self.roles["business"]
        job_role = self.roles["job_role"]

        return (
            f"{subject.name} started a new job as a "
            f"{job_role.name} at {business.name}."
        )


class StartBusiness(LifeEvent):
    """Character starts a specific business."""

    def __init__(
        self,
        subject: GameObject,
        business: GameObject,
        district: GameObject,
        settlement: GameObject,
    ) -> None:
        super().__init__(
            world=subject.world,
            roles=[
                EventRole("subject", subject, True),
                EventRole("business", business, True),
                EventRole("district", district),
                EventRole("settlement", settlement),
            ],
        )

    @staticmethod
    @event_consideration
    def has_job_consideration(event: StartBusiness) -> float:
        """check if the character already has a job."""
        if event.roles["subject"].has_component(Occupation):
            return 0

        return -1

    @staticmethod
    @event_consideration
    def boldness_consideration(event: StartBusiness) -> float:
        """Considers the subject's boldness stat."""
        return get_stat(event.roles["subject"], "boldness").normalized

    @staticmethod
    @event_consideration
    def reliability_consideration(event: StartBusiness) -> float:
        """Considers the subjects reliability stat."""
        return get_stat(event.roles["subject"], "reliability").normalized

    @staticmethod
    @event_consideration
    def time_unemployed_consideration(event: StartBusiness) -> float:
        """Calculate consideration score based on the amount of time unemployed."""
        subject = event.roles["subject"]

        if unemployed := subject.try_component(Unemployed):
            current_date = subject.world.resource_manager.get_resource(SimDate)
            months_unemployed = (
                current_date.total_months - unemployed.timestamp.total_months
            )
            return min(1.0, float(months_unemployed) / 6.0)

        return -1

    def execute(self) -> None:
        character = self.roles["subject"]
        business = self.roles["business"]
        business_comp = business.get_component(Business)
        job_role = business_comp.owner_role
        current_date = self.world.resource_manager.get_resource(SimDate)

        assert job_role is not None

        character.add_component(
            Occupation(business=business, start_date=current_date, job_role=job_role)
        )

        add_frequented_location(character, business)

        business_comp.set_owner(character)

        business.remove_component(PendingOpening)
        business.add_component(OpenForBusiness())
        business.add_component(OpenToPublic())

        if character.has_component(Unemployed):
            character.remove_component(Unemployed)

    @classmethod
    def instantiate(cls, subject: GameObject, **kwargs: Any) -> LifeEvent | None:
        world = subject.world

        pending_businesses: list[Business] = [
            business
            for _, (business, _, _) in world.get_components(
                (Business, Active, PendingOpening)
            )
        ]

        rng = world.resource_manager.get_resource(random.Random)

        eligible_businesses: list[tuple[Business, JobRole]] = []

        for business in pending_businesses:
            owner_role = business.owner_role
            assert owner_role

            if owner_role.check_requirements(subject):
                eligible_businesses.append((business, owner_role))

        if eligible_businesses:
            chosen_business, owner_role = rng.choice(eligible_businesses)

            chosen_business.gameobject.remove_component(PendingOpening)
            chosen_business.gameobject.add_component(OpenForBusiness())

            return StartBusiness(
                subject=subject,
                business=chosen_business.gameobject,
                district=chosen_business.district,
                settlement=chosen_business.district.get_component(District).settlement,
            )

        return None

    def __str__(self) -> str:
        subject = self.roles["subject"]
        business = self.roles["business"]
        district = self.roles["district"]
        settlement = self.roles["settlement"]

        return (
            f"{subject.name} opened a new business, "
            f"{business.name}, in the {district.name} district of "
            f"{settlement.name}."
        )


class StartDating(LifeEvent):
    """Event dispatched when two characters start dating."""

    is_logged = True
    base_probability = 0.5

    def __init__(self, subject: GameObject, partner: GameObject) -> None:
        super().__init__(
            world=subject.world,
            roles=[
                EventRole("subject", subject, True),
                EventRole("partner", partner, True),
            ],
        )

    def execute(self) -> None:
        subject_0 = self.roles["subject"]
        partner = self.roles["partner"]

        add_trait(get_relationship(subject_0, partner), "dating")
        add_trait(get_relationship(partner, subject_0), "dating")

    @staticmethod
    @event_consideration
    def subject_has_crush(event: StartDating) -> float:
        """Consider if the subject has a crush on the other person."""
        subject = event.roles["subject"]
        other = event.roles["partner"]

        if has_trait(get_relationship(subject, other), "crush"):
            return 0.7

        return 0.2

    @staticmethod
    @event_consideration
    def other_has_crush(event: StartDating) -> float:
        """Consider if the other person has a crush on the subject."""
        subject = event.roles["subject"]
        other = event.roles["partner"]

        if has_trait(get_relationship(other, subject), "crush"):
            return 0.7

        return 0.2

    @staticmethod
    @event_consideration
    def romance_to_partner(event: StartDating) -> float:
        """Consider the romance from the partner to the subject."""
        return (
            get_stat(
                get_relationship(event.roles["subject"], event.roles["partner"]),
                "romance",
            ).normalized
            ** 2
        )

    @staticmethod
    @event_consideration
    def romance_to_subject(event: StartDating) -> float:
        """Consider the romance from the partner to the subject."""
        return (
            get_stat(
                get_relationship(event.roles["partner"], event.roles["subject"]),
                "romance",
            ).normalized
            ** 2
        )

    @staticmethod
    @event_consideration
    def partner_already_dating(event: StartDating) -> float:
        """Consider if the partner is already dating someone."""
        if len(get_relationships_with_traits(event.roles["partner"], "dating")) > 0:
            return 0.05

        if len(get_relationships_with_traits(event.roles["partner"], "spouse")) > 0:
            return 0.05

        return -1

    @classmethod
    def instantiate(cls, subject: GameObject, **kwargs: Any) -> LifeEvent | None:
        if subject.get_component(Character).life_stage <= LifeStage.ADOLESCENT:
            return None

        if len(get_relationships_with_traits(subject, "dating")) > 0:
            return None

        relationships = list(subject.get_component(Relationships).outgoing.items())

        potential_partners: list[GameObject] = []
        partner_weights: list[float] = []

        for target, relationship in relationships:
            if target.get_component(Character).life_stage <= LifeStage.ADOLESCENT:
                continue

            romance = get_stat(relationship, "romance").normalized

            if romance > 0:
                potential_partners.append(target)
                partner_weights.append(romance)

        if potential_partners:
            rng = subject.world.resource_manager.get_resource(random.Random)

            chosen_partner = rng.choices(
                potential_partners, weights=partner_weights, k=1
            )[0]

            return StartDating(
                subject=subject,
                partner=chosen_partner,
            )

        return None

    def __str__(self) -> str:
        subject_0 = self.roles["subject"]
        partner = self.roles["partner"]
        return f"{subject_0.name} and {partner.name} started dating."


class GetMarried(LifeEvent):
    """Event dispatched when two characters get married."""

    def __init__(self, subject: GameObject, partner: GameObject) -> None:
        super().__init__(
            world=subject.world,
            roles=[
                EventRole("subject", subject, True),
                EventRole("subject", partner, True),
            ],
        )

    @staticmethod
    @event_consideration
    def life_stage_consideration(event: GetMarried) -> float:
        """Check the life stage of both partners"""
        subject_0, subject_1 = event.roles.get_all("subject")

        subject_0_life_stage = subject_0.get_component(Character).life_stage
        subject_1_life_stage = subject_1.get_component(Character).life_stage

        if (
            subject_0_life_stage < LifeStage.YOUNG_ADULT
            or subject_1_life_stage < LifeStage.YOUNG_ADULT
        ):
            return 0.0

        if (
            subject_0_life_stage > LifeStage.ADULT
            or subject_1_life_stage > LifeStage.ADULT
        ):
            return 0.05

        return -1

    @staticmethod
    @event_consideration
    def romance_to_partner(event: StartDating) -> float:
        """Consider the romance from the partner to the subject."""
        subject_0, subject_1 = event.roles.get_all("subject")

        return get_stat(get_relationship(subject_0, subject_1), "romance").normalized

    @staticmethod
    @event_consideration
    def romance_to_subject(event: StartDating) -> float:
        """Consider the romance from the partner to the subject."""
        subject_0, subject_1 = event.roles.get_all("subject")

        return get_stat(get_relationship(subject_1, subject_0), "romance").normalized

    @classmethod
    def instantiate(cls, subject: GameObject, **kwargs: Any) -> LifeEvent | None:
        subject_life_stage = subject.get_component(Character).life_stage

        if subject_life_stage < LifeStage.YOUNG_ADULT:
            return None

        if len(get_relationships_with_traits(subject, "spouse")) > 0:
            return None

        dating_relationships = get_relationships_with_traits(subject, "dating")

        rng = subject.world.resource_manager.get_resource(random.Random)
        rng.shuffle(dating_relationships)

        for relationship in dating_relationships:
            partner = relationship.get_component(Relationship).target

            if partner.get_component(Character).life_stage < LifeStage.YOUNG_ADULT:
                continue

            return GetMarried(subject=subject, partner=partner)

        return None

    def execute(self) -> None:
        subject_0, subject_1 = self.roles.get_all("subject")

        remove_trait(get_relationship(subject_0, subject_1), "dating")
        remove_trait(get_relationship(subject_1, subject_0), "dating")

        add_trait(get_relationship(subject_0, subject_1), "spouse")
        add_trait(get_relationship(subject_1, subject_0), "spouse")

        # Update residences
        shared_residence = subject_0.get_component(Resident).residence

        ChangeResidenceEvent(
            subject_1, new_residence=shared_residence, is_owner=True
        ).dispatch()

        for rel in get_relationships_with_traits(subject_1, "child", "live_together"):
            target = rel.get_component(Relationship).target
            ChangeResidenceEvent(target, new_residence=shared_residence).dispatch()

        # Update step sibling relationships
        for rel_0 in get_relationships_with_traits(subject_0, "child"):
            if not rel_0.is_active:
                continue

            child_0 = rel_0.get_component(Relationship).target

            for rel_1 in get_relationships_with_traits(subject_1, "child"):
                if not rel_1.is_active:
                    continue

                child_1 = rel_1.get_component(Relationship).target

                add_trait(get_relationship(child_0, child_1), "step_sibling")
                add_trait(get_relationship(child_0, child_1), "sibling")
                add_trait(get_relationship(child_1, child_0), "step_sibling")
                add_trait(get_relationship(child_1, child_0), "sibling")

        # Update relationships parent/child relationships
        for rel in get_relationships_with_traits(subject_0, "child"):
            if rel.is_active:
                child = rel.get_component(Relationship).target
                if not has_trait(get_relationship(subject_1, child), "child"):
                    add_trait(get_relationship(subject_1, child), "child")
                    add_trait(get_relationship(subject_1, child), "step_child")
                    add_trait(get_relationship(child, subject_1), "parent")
                    add_trait(get_relationship(child, subject_1), "step_parent")

        for rel in get_relationships_with_traits(subject_1, "child"):
            if rel.is_active:
                child = rel.get_component(Relationship).target
                if not has_trait(get_relationship(subject_0, child), "child"):
                    add_trait(get_relationship(subject_0, child), "child")
                    add_trait(get_relationship(subject_0, child), "step_child")
                    add_trait(get_relationship(child, subject_0), "parent")
                    add_trait(get_relationship(child, subject_0), "step_parent")

    def __str__(self) -> str:
        subject_0, subject_1 = self.roles.get_all("subject")

        return f"{subject_0.name} and {subject_1.name} got married."


class GetDivorced(LifeEvent):
    """Dispatched to officially divorce two married characters."""

    def __init__(self, subject: GameObject, ex_spouse: GameObject) -> None:
        super().__init__(
            world=subject.world,
            roles=[
                EventRole("subject", subject, True),
                EventRole("ex_spouse", ex_spouse, True),
            ],
        )

    @staticmethod
    @event_consideration
    def romance_to_spouse(event: GetDivorced) -> float:
        """Consider how in-love the subject is with the ex_spouse"""
        return (
            1.0
            - get_stat(
                get_relationship(event.roles["subject"], event.roles["ex_spouse"]),
                "romance",
            ).normalized
        )

    @classmethod
    def instantiate(cls, subject: GameObject, **kwargs: Any) -> Optional[LifeEvent]:
        spousal_relationships = get_relationships_with_traits(subject, "spouse")

        rng = subject.world.resource_manager.get_resource(random.Random)

        rng.shuffle(spousal_relationships)

        for relationship in spousal_relationships:
            if not relationship.has_component(Active):
                continue

            partner = relationship.get_component(Relationship).target

            return GetDivorced(subject=subject, ex_spouse=partner)

        return None

    def execute(self) -> None:
        initiator = self.roles["subject"]
        ex_spouse = self.roles["ex_spouse"]

        remove_trait(get_relationship(initiator, ex_spouse), "spouse")
        remove_trait(get_relationship(ex_spouse, initiator), "spouse")

        add_trait(get_relationship(initiator, ex_spouse), "ex_spouse")
        add_trait(get_relationship(ex_spouse, initiator), "ex_spouse")

        get_stat(get_relationship(ex_spouse, initiator), "romance").base_value -= 25

        # initiator finds new place to live or departs
        vacant_housing = initiator.world.get_components((ResidentialUnit, Vacant))

        if vacant_housing:
            _, (residence, _) = vacant_housing[0]
            ChangeResidenceEvent(
                initiator, new_residence=residence.gameobject, is_owner=True
            ).dispatch()

        else:
            ChangeResidenceEvent(initiator, new_residence=None).dispatch()
            DepartSettlement(initiator).dispatch()

    def __str__(self) -> str:
        initiator = self.roles["subject"]
        ex_spouse = self.roles["ex_spouse"]

        return f"{initiator.name} divorced from {ex_spouse.name}."


class BreakUp(LifeEvent):
    """Dispatched to officially break up a dating relationship between characters."""

    def __init__(self, subject: GameObject, ex_partner: GameObject) -> None:
        super().__init__(
            world=subject.world,
            roles=[
                EventRole("subject", subject, True),
                EventRole("ex_partner", ex_partner, True),
            ],
        )

    @staticmethod
    @event_consideration
    def romance_to_partner(event: StartDating) -> float:
        """Consider the romance from the partner to the subject."""
        return (
            1.0
            - get_stat(
                get_relationship(event.roles["subject"], event.roles["ex_partner"]),
                "romance",
            ).normalized
        )

    @classmethod
    def instantiate(cls, subject: GameObject, **kwargs: Any) -> LifeEvent | None:
        dating_relationships = get_relationships_with_traits(subject, "dating")

        rng = subject.world.resource_manager.get_resource(random.Random)

        if dating_relationships:
            relationship = rng.choice(dating_relationships)
            return BreakUp(
                subject=subject,
                ex_partner=relationship.get_component(Relationship).target,
            )

        return None

    def execute(self) -> None:
        initiator = self.roles["subject"]
        ex_partner = self.roles["ex_partner"]

        remove_trait(get_relationship(initiator, ex_partner), "dating")
        remove_trait(get_relationship(ex_partner, initiator), "dating")

        add_trait(get_relationship(initiator, ex_partner), "ex_partner")
        add_trait(get_relationship(ex_partner, initiator), "ex_partner")

        get_stat(get_relationship(ex_partner, initiator), "romance").base_value -= 15

    def __str__(self) -> str:
        initiator = self.roles["subject"]
        ex_partner = self.roles["ex_partner"]

        return f"{initiator.name} broke up with " f"{ex_partner.name}."


class GetPregnant(LifeEvent):
    """Characters have a chance of getting pregnant while in romantic relationships."""

    base_probability = 0.5

    def __init__(
        self,
        subject: GameObject,
        partner: GameObject,
    ) -> None:
        super().__init__(
            world=subject.world,
            roles=[EventRole("subject", subject, True), EventRole("partner", partner)],
        )

    @staticmethod
    @event_consideration
    def check_if_pregnant(event: GetPregnant) -> float:
        """Check if the subject is already pregnant"""
        if event.roles["subject"].has_component(Pregnant):
            return 0.0
        return -1.0

    @staticmethod
    @event_consideration
    def proper_sex_consideration(event: GetPregnant) -> float:
        """Check that characters are the right sex to procreate."""
        subject = event.roles["subject"]
        partner = event.roles["partner"]

        if subject.get_component(Character).sex == Sex.MALE:
            return 0.0

        if partner.get_component(Character).sex == Sex.FEMALE:
            return 0.0

        return -1

    @staticmethod
    @event_consideration
    def fertility_consideration(event: GetPregnant) -> float:
        """Check the fertility of the subject."""
        return get_stat(event.roles["subject"], "fertility").value

    @staticmethod
    @event_consideration
    def partner_fertility_consideration(event: GetPregnant) -> float:
        """Check fertility of the partner."""
        return get_stat(event.roles["partner"], "fertility").value

    @classmethod
    def instantiate(cls, subject: GameObject, **kwargs: Any) -> LifeEvent | None:
        marriages = get_relationships_with_traits(subject, "spouse")

        for relationship in marriages:
            partner = relationship.get_component(Relationship).target

            if partner.get_component(Character).sex != Sex.MALE:
                continue

            return GetPregnant(subject=subject, partner=partner)

        return None

    def execute(self) -> None:
        subject = self.roles["subject"]
        partner = self.roles["partner"]

        due_date = self.world.resource_manager.get_resource(SimDate).copy()
        due_date.increment(months=9)

        subject.add_component(Pregnant(partner=partner, due_date=due_date))

    def __str__(self) -> str:
        subject = self.roles["subject"]
        partner = self.roles["partner"]

        return f"{subject.name} got pregnant by {partner.name}."


class Retire(LifeEvent):
    """Event dispatched when a character retires."""

    def __init__(
        self,
        subject: GameObject,
        business: GameObject,
        job_role: GameObject,
    ) -> None:
        super().__init__(
            world=subject.world,
            roles=[
                EventRole("subject", subject, log_event=True),
                EventRole("business", business),
                EventRole("job_role", job_role),
            ],
        )

    @staticmethod
    @event_consideration
    def life_stage_consideration(event: Retire) -> float:
        """Calculate probability of retiring based on life stage."""
        subject = event.roles["subject"]
        life_stage = subject.get_component(Character).life_stage

        if life_stage < LifeStage.SENIOR:
            return 0.01

        return 0.8

    @classmethod
    def instantiate(cls, subject: GameObject, **kwargs: Any) -> LifeEvent | None:
        if occupation := subject.try_component(Occupation):
            return Retire(
                subject=subject,
                business=occupation.business,
                job_role=occupation.job_role.gameobject,
            )

        return None

    def execute(self) -> None:
        subject = self.roles["subject"]
        business = self.roles["business"]
        job_role = self.roles["job_role"]

        add_trait(subject, "retired")

        LeaveJob(subject=subject, business=business, job_role=job_role).dispatch()

    def __str__(self) -> str:
        character = self.roles["subject"]
        occupation = self.roles["job_role"]
        business = self.roles["business"]

        return (
            f"{character.name} retired from their "
            f"position as {occupation.name} at {business.name}."
        )


class DepartDueToUnemployment(LifeEvent):
    """Character leave the settlement and the simulation."""

    base_probability = 0.3

    def __init__(self, subject: GameObject, reason: str = "") -> None:
        super().__init__(
            world=subject.world, roles=[EventRole("subject", subject)], reason=reason
        )

    @classmethod
    def instantiate(cls, subject: GameObject, **kwargs: Any) -> LifeEvent | None:
        return DepartDueToUnemployment(subject)

    @staticmethod
    @event_consideration
    def employment_spouse_consideration(event: DepartDueToUnemployment) -> float:
        """Calculate consideration score for if the character is married."""
        subject = event.roles["subject"]
        if len(get_relationships_with_traits(subject, "spouse")) > 0:
            return 0.7
        return -1

    @staticmethod
    @event_consideration
    def employment_children_consideration(event: DepartDueToUnemployment) -> float:
        """Calculate a consideration score based on a character's number of children/"""
        subject = event.roles["subject"]

        child_count = len(get_relationships_with_traits(subject, "child"))

        if child_count != 0:
            return min(1.0, child_count / 5.0)

        return -1

    @staticmethod
    @event_consideration
    def has_occupation_consideration(event: DepartDueToUnemployment) -> float:
        """Calculate consideration score for if the character already has a job"""
        subject = event.roles["subject"]
        if subject.has_component(Occupation):
            return 0.0

        return -1

    @staticmethod
    @event_consideration
    def reliability_consideration(event: DepartDueToUnemployment) -> float:
        """Calculate consideration score for a character's reliability"""
        return get_stat(event.roles["subject"], "reliability").normalized

    @staticmethod
    @event_consideration
    def time_unemployed_consideration(event: DepartDueToUnemployment) -> float:
        """Calculate consideration score based on the amount of time unemployed."""
        subject = event.roles["subject"]
        if unemployed := subject.try_component(Unemployed):
            current_date = subject.world.resource_manager.get_resource(SimDate)
            months_unemployed = (
                current_date.total_months - unemployed.timestamp.total_months
            )
            return min(1.0, float(months_unemployed) / 6.0)
        return -1

    @staticmethod
    @event_consideration
    def spouse_employment_consideration(event: DepartDueToUnemployment) -> float:
        """Veto if spouse has a job"""
        subject = event.roles["subject"]

        spousal_relationships = get_relationships_with_traits(subject, "spouse")

        # Depart if none of their spouses has a job either
        if any(
            rel.get_component(Relationship).target.has_component(Occupation)
            for rel in spousal_relationships
        ):
            return 0

        return -1

    def execute(self) -> None:
        character = self.roles["subject"]
        DepartSettlement(subject=character, reason="unemployment").dispatch()


class BecomeFriends(LifeEvent):
    """Two characters become friends."""

    base_probability = 0.5

    def __init__(self, subject: GameObject, other: GameObject) -> None:
        super().__init__(
            world=subject.world,
            roles=(
                EventRole("subject", subject, True),
                EventRole("other", other, True),
            ),
        )

    @staticmethod
    @event_consideration
    def other_friend_count_consideration(event: BecomeFriends) -> float:
        """Consider the number of friends the other character already has."""
        return (
            1.0
            - min(
                len(get_relationships_with_traits(event.roles["other"], "friend"))
                / 8.0,
                1.0,
            )
        ) ** 2

    @staticmethod
    @event_consideration
    def friend_count_consideration(event: BecomeFriends) -> float:
        """Consider the number of friends the subject already has."""
        return (
            1.0
            - min(
                len(get_relationships_with_traits(event.roles["subject"], "friend"))
                / 8.0,
                1.0,
            )
        ) ** 2

    @staticmethod
    @event_consideration
    def other_reputation_consideration(event: BecomeFriends) -> float:
        """Consider the reputation from the subject to the other person."""
        return (
            get_stat(
                get_relationship(event.roles["other"], event.roles["subject"]),
                "reputation",
            ).normalized
            ** 2
        )

    @staticmethod
    @event_consideration
    def subject_reputation_consideration(event: BecomeFriends) -> float:
        """Consider the reputation from the subject to the other person."""
        return (
            get_stat(
                get_relationship(event.roles["subject"], event.roles["other"]),
                "reputation",
            ).normalized
            ** 2
        )

    @staticmethod
    @event_consideration
    def are_enemies(event: BecomeFriends) -> float:
        """Consider if they are enemies."""
        if has_trait(
            get_relationship(event.roles["other"], event.roles["subject"]), "enemy"
        ):
            return 0.01
        return -1

    @classmethod
    def instantiate(cls, subject: GameObject, **kwargs: Any) -> LifeEvent | None:
        if not subject.has_component(Character):
            # Friendships can only form between people. This is here for future proofing
            # incase life events can ever be triggers by more than characters
            return None

        options: list[GameObject] = []
        scores: list[float] = []

        for target, rel in subject.get_component(Relationships).outgoing.items():
            # Only allow friendships between characters
            if not target.has_component(Character):
                continue

            if target.is_active is False:
                continue

            if has_trait(rel, "friend"):
                continue

            if get_stat(rel, "reputation").value <= 0:
                continue

            score = get_stat(rel, "reputation").normalized
            if score > 0:
                options.append(target)
                scores.append(score)

        if not options:
            return None

        rng = subject.world.resource_manager.get_resource(random.Random)

        choice = rng.choices(options, weights=scores, k=1)[0]

        return BecomeFriends(subject, choice)

    def execute(self) -> None:
        subject = self.roles["subject"]
        other = self.roles["other"]
        add_trait(get_relationship(subject, other), "friend")
        add_trait(get_relationship(other, subject), "friend")

    def __str__(self) -> str:
        subject = self.roles["subject"]
        other = self.roles["other"]
        return f"{subject.name} and {other.name} became friends."


class DissolveFriendship(LifeEvent):
    """Two characters stop being friends."""

    base_probability = 0.2

    def __init__(self, subject: GameObject, other: GameObject) -> None:
        super().__init__(
            world=subject.world,
            roles=(
                EventRole("subject", subject, True),
                EventRole("other", other, True),
            ),
        )

    @staticmethod
    @event_consideration
    def other_reputation_consideration(event: BecomeFriends) -> float:
        """Consider the reputation from the subject to the other person."""
        return (
            1
            - get_stat(
                get_relationship(event.roles["other"], event.roles["subject"]),
                "reputation",
            ).normalized
        )

    @staticmethod
    @event_consideration
    def subject_reputation_consideration(event: BecomeFriends) -> float:
        """Consider the reputation from the subject to the other person."""
        return (
            1
            - get_stat(
                get_relationship(event.roles["subject"], event.roles["other"]),
                "reputation",
            ).normalized
        )

    @classmethod
    def instantiate(cls, subject: GameObject, **kwargs: Any) -> LifeEvent | None:
        if not subject.has_component(Character):
            # Friendships can only form between people. This is here for future proofing
            # incase life events can ever be triggers by more than characters
            return None

        options: list[GameObject] = []
        scores: list[float] = []

        for target, rel in subject.get_component(Relationships).outgoing.items():
            # Only allow friendships between characters
            if not target.has_component(Character):
                continue

            if not has_trait(rel, "friend"):
                continue

            if target.is_active is False:
                continue

            score = 1.0 - get_stat(rel, "reputation").normalized
            if score > 0:
                options.append(target)
                scores.append(score)

        if not options:
            return None

        rng = subject.world.resource_manager.get_resource(random.Random)

        choice = rng.choices(options, weights=scores, k=1)[0]

        return DissolveFriendship(subject, choice)

    def execute(self) -> None:
        subject = self.roles["subject"]
        other = self.roles["other"]
        remove_trait(get_relationship(subject, other), "friend")
        remove_trait(get_relationship(other, subject), "friend")

    def __str__(self) -> str:
        subject = self.roles["subject"]
        other = self.roles["other"]
        return f"{subject.name} and {other.name} stopped being friends."


class BecomeEnemies(LifeEvent):
    """Two characters become enemies."""

    base_probability = 0.5

    def __init__(self, subject: GameObject, other: GameObject) -> None:
        super().__init__(
            world=subject.world,
            roles=(
                EventRole("subject", subject, True),
                EventRole("other", other, True),
            ),
        )

    @staticmethod
    @event_consideration
    def are_friends(event: BecomeEnemies) -> float:
        """Consider if they are friends."""
        if has_trait(
            get_relationship(event.roles["other"], event.roles["subject"]), "friend"
        ):
            return 0.01
        return -1

    @staticmethod
    @event_consideration
    def other_reputation_consideration(event: BecomeEnemies) -> float:
        """Consider the reputation from the subject to the other person."""
        return (
            1
            - get_stat(
                get_relationship(event.roles["other"], event.roles["subject"]),
                "reputation",
            ).normalized
        ) ** 2

    @staticmethod
    @event_consideration
    def subject_reputation_consideration(event: BecomeEnemies) -> float:
        """Consider the reputation from the subject to the other person."""
        return (
            1
            - get_stat(
                get_relationship(event.roles["subject"], event.roles["other"]),
                "reputation",
            ).normalized
        ) ** 2

    @classmethod
    def instantiate(cls, subject: GameObject, **kwargs: Any) -> LifeEvent | None:
        if not subject.has_component(Character):
            # Enmity can only form between people. This is here for future proofing
            # incase life events can ever be triggers by more than characters
            return None

        options: list[GameObject] = []
        scores: list[float] = []

        for target, rel in subject.get_component(Relationships).outgoing.items():
            # Only allow enmity between characters
            if not target.has_component(Character):
                continue

            if target.is_active is False:
                continue

            if has_trait(rel, "enemy"):
                continue

            if get_stat(rel, "reputation").value >= 0:
                continue

            score = 1 - get_stat(rel, "reputation").normalized
            if score > 0:
                options.append(target)
                scores.append(score)

        if not options:
            return None

        rng = subject.world.resource_manager.get_resource(random.Random)

        choice = rng.choices(options, weights=scores, k=1)[0]

        return BecomeEnemies(subject, choice)

    def execute(self) -> None:
        subject = self.roles["subject"]
        other = self.roles["other"]
        add_trait(get_relationship(subject, other), "enemy")
        add_trait(get_relationship(other, subject), "enemy")

    def __str__(self) -> str:
        subject = self.roles["subject"]
        other = self.roles["other"]
        return f"{subject.name} and {other.name} became enemies."


class DissolveEnmity(LifeEvent):
    """Two characters stop being enemies."""

    base_probability = 0.2

    def __init__(self, subject: GameObject, other: GameObject) -> None:
        super().__init__(
            world=subject.world,
            roles=(
                EventRole("subject", subject, True),
                EventRole("other", other, True),
            ),
        )

    @staticmethod
    @event_consideration
    def other_reputation_consideration(event: BecomeFriends) -> float:
        """Consider the reputation from the subject to the other person."""
        return get_stat(
            get_relationship(event.roles["other"], event.roles["subject"]),
            "reputation",
        ).normalized

    @staticmethod
    @event_consideration
    def subject_reputation_consideration(event: BecomeFriends) -> float:
        """Consider the reputation from the subject to the other person."""
        return get_stat(
            get_relationship(event.roles["subject"], event.roles["other"]),
            "reputation",
        ).normalized

    @classmethod
    def instantiate(cls, subject: GameObject, **kwargs: Any) -> LifeEvent | None:
        if not subject.has_component(Character):
            # Friendships can only form between people. This is here for future proofing
            # incase life events can ever be triggers by more than characters
            return None

        options: list[GameObject] = []
        scores: list[float] = []

        for target, rel in subject.get_component(Relationships).outgoing.items():
            # Only allow friendships between characters
            if not target.has_component(Character):
                continue

            if target.is_active is False:
                continue

            if not has_trait(rel, "enemy"):
                continue

            score = get_stat(rel, "reputation").normalized
            if score > 0:
                options.append(target)
                scores.append(score)

        if not options:
            return None

        rng = subject.world.resource_manager.get_resource(random.Random)

        choice = rng.choices(options, weights=scores, k=1)[0]

        return DissolveEnmity(subject, choice)

    def execute(self) -> None:
        subject = self.roles["subject"]
        other = self.roles["other"]
        remove_trait(get_relationship(subject, other), "enemy")
        remove_trait(get_relationship(other, subject), "enemy")

    def __str__(self) -> str:
        subject = self.roles["subject"]
        other = self.roles["other"]
        return f"{subject.name} and {other.name} stopped being enemies."


class FormCrush(LifeEvent):
    """A character forms a new crush on someone."""

    base_probability = 0.2

    def __init__(self, subject: GameObject, other: GameObject) -> None:
        super().__init__(
            world=subject.world,
            roles=(
                EventRole("subject", subject, True),
                EventRole("other", other, False),
            ),
        )

    @staticmethod
    @event_consideration
    def current_crush_consideration(event: FormCrush) -> float:
        """Consider a character's current crush."""
        subject = event.roles["subject"]
        crush_relationships = get_relationships_with_traits(subject, "crush")

        if crush_relationships:
            relationship = crush_relationships[0]
            if relationship.is_active:
                return 1 - get_stat(relationship, "romance").normalized

        return -1

    @staticmethod
    @event_consideration
    def romance_consideration(event: FormCrush) -> float:
        """Consider a character's romance value."""
        return (
            get_stat(
                get_relationship(event.roles["subject"], event.roles["other"]),
                "romance",
            ).normalized
            ** 2
        )

    @classmethod
    def instantiate(cls, subject: GameObject, **kwargs: Any) -> LifeEvent | None:
        if not subject.has_component(Character):
            return None

        options: list[GameObject] = []
        scores: list[float] = []

        for target, rel in subject.get_component(Relationships).outgoing.items():
            # Only allow friendships between characters
            if not target.has_component(Character):
                continue

            if target.is_active is False:
                continue

            if has_trait(rel, "crush"):
                continue

            if get_stat(rel, "romance").value <= 0:
                continue

            score = get_stat(rel, "romance").normalized
            if score > 0:
                options.append(target)
                scores.append(score)

        if not options:
            return None

        rng = subject.world.resource_manager.get_resource(random.Random)

        choice = rng.choices(options, weights=scores, k=1)[0]

        return FormCrush(subject, choice)

    def execute(self) -> None:
        subject = self.roles["subject"]
        other = self.roles["other"]

        # remove existing crushes
        for rel in get_relationships_with_traits(subject, "crush"):
            remove_trait(rel, "crush")

        add_trait(get_relationship(subject, other), "crush")

    def __str__(self) -> str:
        subject = self.roles["subject"]
        other = self.roles["other"]
        return f"{subject.name} formed a crush on {other.name}"


class TryFindOwnPlace(LifeEvent):
    """Adults living with parents will try to find their own residence."""

    base_probability = 0.4

    def __init__(self, subject: GameObject) -> None:
        super().__init__(
            world=subject.world,
            roles=(EventRole("subject", subject, True),),
        )

    @staticmethod
    @event_consideration
    def boldness_consideration(event: StartANewJob) -> float:
        """Considers the subject's boldness stat."""
        return get_stat(event.roles["subject"], "boldness").normalized

    @staticmethod
    @event_consideration
    def reliability_consideration(event: StartANewJob) -> float:
        """Considers the subjects reliability stat."""
        return get_stat(event.roles["subject"], "reliability").normalized

    def execute(self) -> None:
        subject = self.roles["subject"]

        vacant_housing = subject.world.get_components((ResidentialUnit, Vacant))

        if vacant_housing:
            _, (residence, _) = vacant_housing[0]
            ChangeResidenceEvent(
                subject, new_residence=residence.gameobject, is_owner=True
            ).dispatch()

        else:
            ChangeResidenceEvent(subject, new_residence=None).dispatch()
            DepartSettlement(subject).dispatch()

    @classmethod
    def instantiate(cls, subject: GameObject, **kwargs: Any) -> LifeEvent | None:
        parents_they_live_with = get_relationships_with_traits(
            subject, "parent", "live_together"
        )
        owns_home = False

        if resident := subject.try_component(Resident):
            owns_home = resident.residence.get_component(ResidentialUnit).is_owner(
                subject
            )

        if len(parents_they_live_with) > 0 and owns_home is False:
            return TryFindOwnPlace(subject)

        return None

    def __str__(self) -> str:
        subject = self.roles["subject"]
        return f"{subject.name} moved out of their parent's home."


class JobPromotion(LifeEvent):
    """The character is promoted at their job from a lower role to a higher role."""

    base_probability = 0.5

    def __init__(
        self,
        subject: GameObject,
        business: GameObject,
        old_role: GameObject,
        new_role: GameObject,
    ) -> None:
        super().__init__(
            world=subject.world,
            roles=(
                EventRole("subject", subject, True),
                EventRole("business", business),
                EventRole("old_role", old_role),
                EventRole("new_role", new_role),
            ),
        )

    @staticmethod
    @event_consideration
    def relationship_with_owner(event: LifeEvent) -> float:
        """Considers the subject's reputation with the business' owner."""
        subject = event.roles["subject"]
        business_owner = event.roles["business"].get_component(Business).owner

        if business_owner is not None:
            return get_stat(
                get_relationship(business_owner, subject),
                "reputation",
            ).normalized

        return -1

    @staticmethod
    @event_consideration
    def boldness_consideration(event: LifeEvent) -> float:
        """Considers the subject's boldness stat."""
        return get_stat(event.roles["subject"], "boldness").normalized

    @staticmethod
    @event_consideration
    def reliability_consideration(event: LifeEvent) -> float:
        """Considers the subjects reliability stat."""
        return get_stat(event.roles["subject"], "reliability").normalized

    def execute(self) -> None:
        character = self.roles["subject"]
        business = self.roles["business"]
        new_role = self.roles["new_role"]

        business_data = business.get_component(Business)

        # Remove the old occupation
        character.remove_component(Occupation)

        business_data.remove_employee(character)

        # Add the new occupation
        character.add_component(
            Occupation(
                business=business,
                start_date=self.world.resource_manager.get_resource(SimDate),
                job_role=new_role.get_component(JobRole),
            )
        )

        business_data.add_employee(character, new_role.get_component(JobRole))

    @classmethod
    def instantiate(cls, subject: GameObject, **kwargs: Any) -> LifeEvent | None:
        rng = subject.world.resource_manager.get_resource(random.Random)

        if subject.has_component(Occupation) is False:
            return None

        occupation = subject.get_component(Occupation)
        current_job_level = occupation.job_role.job_level
        business_data = occupation.business.get_component(Business)
        open_positions = business_data.get_open_positions()

        higher_positions = [
            role
            for role in open_positions
            if (role.job_level > current_job_level and role.check_requirements(subject))
        ]

        if len(higher_positions) == 0:
            return None

        # Get the simulation's random number generator
        rng = subject.world.resource_manager.get_resource(random.Random)

        chosen_role = rng.choice(higher_positions)

        return JobPromotion(
            subject=subject,
            business=business_data.gameobject,
            old_role=occupation.job_role.gameobject,
            new_role=chosen_role.gameobject,
        )

    def __str__(self) -> str:
        subject = self.roles["subject"]
        business = self.roles["business"]
        old_role = self.roles["old_role"]
        new_role = self.roles["new_role"]

        return (
            f"{subject.name} was promoted from {old_role.name} to "
            f"{new_role.name} at {business.name}."
        )


class FiredFromJob(LifeEvent):
    """The character is fired from their job."""

    base_probability = 0.5

    def __init__(
        self, subject: GameObject, business: GameObject, job_role: GameObject
    ) -> None:
        super().__init__(
            world=subject.world,
            roles=(
                EventRole("subject", subject, True),
                EventRole("business", business),
                EventRole("job_role", job_role),
            ),
        )

    @staticmethod
    @event_consideration
    def relationship_with_owner(event: LifeEvent) -> float:
        """Considers the subject's reputation with the business' owner."""
        subject = event.roles["subject"]
        business_owner = event.roles["business"].get_component(Business).owner

        if business_owner is not None:
            return (
                1
                - get_stat(
                    get_relationship(business_owner, subject),
                    "reputation",
                ).normalized
            )

        return -1

    @staticmethod
    @event_consideration
    def reliability_consideration(event: LifeEvent) -> float:
        """Considers the subjects reliability stat."""
        return 1 - get_stat(event.roles["subject"], "reliability").normalized

    def execute(self) -> None:
        subject = self.roles["subject"]
        business = self.roles["business"]
        job_role = self.roles["job_role"]

        # Events can dispatch other events
        LeaveJob(
            subject=subject, business=business, job_role=job_role, reason="fired"
        ).dispatch()

        business_data = business.get_component(Business)

        owner = business_data.owner
        if owner is not None:
            get_stat(get_relationship(subject, owner), "reputation").base_value -= 20
            get_stat(get_relationship(owner, subject), "reputation").base_value -= 10

    @classmethod
    def instantiate(cls, subject: GameObject, **kwargs: Any) -> LifeEvent | None:
        if subject.has_component(Occupation) is False:
            return None

        occupation = subject.get_component(Occupation)

        return FiredFromJob(
            subject=subject,
            business=occupation.business,
            job_role=occupation.job_role.gameobject,
        )

    def __str__(self) -> str:
        subject = self.roles["subject"]
        business = self.roles["business"]
        job_role = self.roles["job_role"]

        return (
            f"{subject.name} was fired from their role as a "
            f"{job_role.name} at {business.name}."
        )


def load_plugin(sim: Simulation) -> None:
    """Load plugin content."""

    register_life_event_type(sim, StartANewJob)
    register_life_event_type(sim, StartBusiness)
    register_life_event_type(sim, StartDating)
    register_life_event_type(sim, GetMarried)
    register_life_event_type(sim, GetDivorced)
    register_life_event_type(sim, BreakUp)
    register_life_event_type(sim, GetPregnant)
    register_life_event_type(sim, Retire)
    register_life_event_type(sim, DepartDueToUnemployment)
    register_life_event_type(sim, BecomeFriends)
    register_life_event_type(sim, DissolveFriendship)
    register_life_event_type(sim, BecomeEnemies)
    register_life_event_type(sim, DissolveEnmity)
    register_life_event_type(sim, FormCrush)
    register_life_event_type(sim, TryFindOwnPlace)
    register_life_event_type(sim, FiredFromJob)
    register_life_event_type(sim, JobPromotion)
