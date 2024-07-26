# Copyright (c) 2024, Emperor and contributors
# For license information, please see license.txt



from gym.api import get_gym_membership_cost

def validate(doc, method):
    if not doc.cost:
        doc.cost = get_gym_membership_cost(doc.membership_type)
