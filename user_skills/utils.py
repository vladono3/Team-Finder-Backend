from database.db import db

def get_skills_by_users_id(user_id):
    user_skills = db.get_user_skills()
    skills = db.get_skills()
    user_skills_list = []
    for key in user_skills:
        user_skill = user_skills[key]
        if user_skill.get("user_id") == user_id:
            user_skill_id = user_skill.get("skill_id")
            skill_name = skills.get(user_skill_id, {}).get("name")
            user_skill["skill_name"] = skill_name
            user_skills_list.append(user_skill)
    user_skills_list.sort(key=lambda x: x.get("skill_name", "").lower())
    return user_skills_list

def create_user_skills(data):
    user_skill_data = data.model_dump()
    db.create_user_skills(user_id=user_skill_data.get("user_id"),
                    skill_id=user_skill_data.get("skill_id"),
                    level=user_skill_data.get("level"),
                    created_at=user_skill_data.get("created_at"),
                    experience=user_skill_data.get("experience"))

    return user_skill_data


def update_user_skills(data):
    updated_user_skills = {}
    for user_skill_data in data:
        user_skill_dict = user_skill_data.model_dump()
        user_id = user_skill_dict.get("user_id")
        db.update_user_skill(user_id=user_id,
                             skill_id=user_skill_dict.get("skill_id"),
                             level=user_skill_dict.get("level"),
                             experience=user_skill_dict.get("experience"))
        updated_user_skills = user_skill_dict
    return updated_user_skills


