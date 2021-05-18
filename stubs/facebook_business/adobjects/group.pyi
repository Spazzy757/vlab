from facebook_business.adobjects.abstractcrudobject import AbstractCrudObject as AbstractCrudObject
from facebook_business.adobjects.abstractobject import AbstractObject as AbstractObject
from facebook_business.adobjects.objectparser import ObjectParser as ObjectParser
from facebook_business.api import FacebookRequest as FacebookRequest
from facebook_business.typechecker import TypeChecker as TypeChecker
from typing import Any, Optional

class Group(AbstractCrudObject):
    def __init__(self, fbid: Optional[Any] = ..., parent_id: Optional[Any] = ..., api: Optional[Any] = ...) -> None: ...
    class Field(AbstractObject.Field):
        archived: str = ...
        cover: str = ...
        created_time: str = ...
        description: str = ...
        email: str = ...
        icon: str = ...
        id: str = ...
        link: str = ...
        member_count: str = ...
        member_request_count: str = ...
        name: str = ...
        owner: str = ...
        parent: str = ...
        permissions: str = ...
        privacy: str = ...
        purpose: str = ...
        subdomain: str = ...
        updated_time: str = ...
        venue: str = ...
    class JoinSetting:
        admin_only: str = ...
        anyone: str = ...
        none: str = ...
    class PostPermissions:
        value_0: str = ...
        value_1: str = ...
        value_2: str = ...
    class Purpose:
        casual: str = ...
        close_friends: str = ...
        club: str = ...
        couple: str = ...
        coworkers: str = ...
        custom: str = ...
        deals: str = ...
        ephemeral: str = ...
        event_planning: str = ...
        family: str = ...
        fitness: str = ...
        for_sale: str = ...
        for_work: str = ...
        fraternity: str = ...
        game: str = ...
        health_support: str = ...
        high_school_forum: str = ...
        jobs: str = ...
        learning: str = ...
        mentorship: str = ...
        neighbors: str = ...
        none: str = ...
        oculus: str = ...
        parenting: str = ...
        parents: str = ...
        project: str = ...
        real_world: str = ...
        real_world_at_work: str = ...
        school_class: str = ...
        sorority: str = ...
        sports: str = ...
        study_group: str = ...
        support: str = ...
        teammates: str = ...
        travel_planning: str = ...
        work_announcement: str = ...
        work_demo_group: str = ...
        work_discussion: str = ...
        work_ephemeral: str = ...
        work_feedback: str = ...
        work_for_sale: str = ...
        work_learning: str = ...
        work_mentorship: str = ...
        work_multi_company: str = ...
        work_recruiting: str = ...
        work_social: str = ...
        work_team: str = ...
        work_teamwork: str = ...
        work_vc_call: str = ...
    class GroupType:
        casual: str = ...
        close_friends: str = ...
        club: str = ...
        couple: str = ...
        coworkers: str = ...
        custom: str = ...
        deals: str = ...
        ephemeral: str = ...
        event_planning: str = ...
        family: str = ...
        fitness: str = ...
        for_sale: str = ...
        for_work: str = ...
        fraternity: str = ...
        game: str = ...
        health_support: str = ...
        high_school_forum: str = ...
        jobs: str = ...
        learning: str = ...
        mentorship: str = ...
        neighbors: str = ...
        none: str = ...
        oculus: str = ...
        parenting: str = ...
        parents: str = ...
        project: str = ...
        real_world: str = ...
        real_world_at_work: str = ...
        school_class: str = ...
        sorority: str = ...
        sports: str = ...
        study_group: str = ...
        support: str = ...
        teammates: str = ...
        travel_planning: str = ...
        work_announcement: str = ...
        work_demo_group: str = ...
        work_discussion: str = ...
        work_ephemeral: str = ...
        work_feedback: str = ...
        work_for_sale: str = ...
        work_learning: str = ...
        work_mentorship: str = ...
        work_multi_company: str = ...
        work_recruiting: str = ...
        work_social: str = ...
        work_team: str = ...
        work_teamwork: str = ...
        work_vc_call: str = ...
    class SuggestionCategory:
        event: str = ...
        messenger: str = ...
        work: str = ...
        workplace: str = ...
        workplace_1_1: str = ...
        workplace_manager: str = ...
    def api_get(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def api_update(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def delete_admins(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def create_admin(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_albums(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def create_album(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_docs(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_events(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def create_feed(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_groups(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def create_group(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_live_videos(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def create_live_video(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def delete_members(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def create_member(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_opted_in_members(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def create_photo(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_picture(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def get_videos(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
    def create_video(self, fields: Optional[Any] = ..., params: Optional[Any] = ..., batch: Optional[Any] = ..., success: Optional[Any] = ..., failure: Optional[Any] = ..., pending: bool = ...): ...
