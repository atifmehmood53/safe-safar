import Customer.models

import Preference.models

Customer = Customer.models.Customer
PreferenceQuestion = Preference.models.PreferenceQuestion
PreferenceAnswer = Preference.models.PreferenceAnswer
CustomerPreferenceAnswer = Preference.models.CustomerPreferenceAnswer



def populate():

    gender = PreferenceQuestion.objects.create(question="Gender?", description="Gender?", type=PreferenceQuestion.BOOL)

    male = PreferenceAnswer.objects.create(preference_question=gender, answer='Male')
    female = PreferenceAnswer.objects.create(preference_question=gender, answer='Female')

    customer_1 = Customer.objects.create(username='o1', community_score=1.0)

    cpa_1 = CustomerPreferenceAnswer.objects.create(customer=customer_1)
    cpa_1.preference_answers.add(male)


