import json
from typing import Dict

import circles_local_aws_s3_storage_python.StorageConstants as StorageConstants
from circles_local_aws_s3_storage_python.CirclesStorage import circles_storage
from gender_local.src.gender import Gender  # TODO: remove src
from language_local.lang_code import LangCode
from location_local.location_local_crud import LocationLocal
from logger_local.Logger import Logger
from operational_hours_local.src.operational_hours import OperationalHours
from profile_reaction_local.src.profile_reaction import ProfileReactions
from reaction_local.src.reaction import Reaction
from user_context_remote.user_context import UserContext

from .constants_profiles_local import OBJECT_TO_INSERT_CODE
from .profiles_local import ProfilesLocal

# TODO add this import when the PersonsLocal class is ready
# from person_local_python_package.src.person import PersonsLocal, PersonDto

logger = Logger.create_logger(object=OBJECT_TO_INSERT_CODE)

# TODO: Should use range and value exported in person-local-python-package
TEST_PERSON_ID = 50050341  # Temporary until Person class is ready

UserContext().login_using_user_identification_and_password()
user_context = UserContext()


class ComprehensiveProfilesLocal:

    @staticmethod
    def insert(profile_json: str, lang_code: str = user_context.get_curent_lang_code()) -> int:
        logger.start(object={"profile_json": str(profile_json), "lang_code": lang_code})

        try:
            data = json.loads(profile_json)
        except json.JSONDecodeError as exception:
            logger.exception(object={exception})
            raise
        profile_id = location_id = None

        keys = data.keys()
        if "location" in keys:
            location_entry: Dict[str, any] = data["location"]
            location_data: Dict[str, any] = {
                "coordinate": {
                    "latitude": location_entry["coordinate"].get("latitude"),
                    "longitude": location_entry["coordinate"].get("longitude"),
                },
                "address_local_language": location_entry.get("address_local_language"),
                "address_english": location_entry.get("address_english"),
                "postal_code": location_entry.get("postal_code"),
                "plus_code": location_entry.get("plus_code"),
                "neighborhood": location_entry.get("neighborhood"),
                "county": location_entry.get("county"),
                "region": location_entry.get("region"),
                "state": location_entry.get("state"),
                "country": location_entry.get("country")
            }
            location_obj = LocationLocal()
            location_id = location_obj.insert(data=location_data, lang_code=lang_code, is_approved=True)

        person_id = TEST_PERSON_ID  # temporary for test
        # Insert person to db
        if 'person' in keys:
            person_entry: Dict[str, any] = data['person']
            gender_obj = Gender()
            gender_id = gender_obj.get_gender_id_by_title(person_entry.get('gender'))
            person_data: Dict[str, any] = {
                'number': person_entry.get('number'),
                'last_coordinate': person_entry.get('last_coordinate'),

            }
            # TODO: why do we need gender_id and person_data?
            # Person class has errors
            '''
            person_dto = PersonDto(
                person_data.get('number'),
                gender_id, person_data.get('last_coordinate'),
                person_data.get('location_id'))
            person_id = PersonsLocal.insert(person_dto)
            PersonsLocal.insert_person_ml(
                person_id,
                lang_code,
                person_data.get('first_name'),
                person_data.get('last_name'))
            '''

        # Insert profile to db
        if 'profile' in keys:
            profile_entry: Dict[str, any] = data['profile']
            profile_data: Dict[str, any] = {
                'profile_name': profile_entry.get('profile_name'),
                'name_approved': profile_entry.get('name_approved'),
                'lang_code': profile_entry.get('lang_code'),
                'user_id': profile_entry.get('user_id'),
                'is_main': profile_entry.get('is_main'),
                'visibility_id': profile_entry.get('visibility_id'),
                'is_approved': profile_entry.get('is_approved'),
                'profile_type_id': profile_entry.get('profile_type_id'),
                # preferred_lang_code the current preferred language of the user in the specific profile. Default: english
                'preferred_lang_code': profile_entry.get('preferred_lang_code', LangCode.ENGLISH.value),
                'experience_years_min': profile_entry.get('experience_years_min'),
                'main_phone_id': profile_entry.get('main_phone_id'),
                'rip': profile_entry.get('rip'),
                'gender_id': profile_entry.get('gender_id'),
                'stars': profile_entry.get('stars'),
                'last_dialog_workflow_state_id': profile_entry.get('last_dialog_workflow_state_id')
            }
            profiles_local_obj = ProfilesLocal()
            profile_id = profiles_local_obj.insert(person_id, profile_data)

        # Insert storage to db
        if "storage" in keys:
            storage_data = {
                "path": data["storage"].get("path"),
                "filename": data["storage"].get("filename"),
                "region": data["storage"].get("region"),
                "url": data["storage"].get("url"),
                "file_extension": data["storage"].get("file_extension"),
                "file_type": data["storage"].get("file_type")
            }
            storage_obj = circles_storage()
            if storage_data["file_type"] == "Profile Image":
                storage_obj.save_image_in_storage_by_url(
                    storage_data["url"],
                    storage_data["filename"],
                    profile_id, StorageConstants.PROFILE_IMAGE),

        # Insert reaction to db
        if "reaction" in keys:
            reaction_data = {
                "value": data["reaction"].get("value"),
                "image": data["reaction"].get("image"),
                "title": data["reaction"].get("title"),
                "description": data["reaction"].get("description"),
            }
            reaction_obj = Reaction()
            # TODO: remove profile_id parameter from reaction-local insert method
            reaction_id = reaction_obj.insert(reaction_data, profile_id, lang_code)
            # Insert profile-reactions to db
            ProfileReactions.insert(reaction_id, profile_id)

        # Insert operational hours to db
        if location_id and "operational_hours" in keys:
            operational_hours = OperationalHours.create_hours_array(data["operational_hours"])
            operational_hours_obj = OperationalHours()
            operational_hours_obj.insert(profile_id, location_id, operational_hours)

        logger.end(object={"profile_id": profile_id})
        return profile_id
