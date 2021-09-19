import Customer.models

import Preference.models

Customer = Customer.models.Customer
PreferenceQuestion = Preference.models.PreferenceQuestion
PreferenceAnswer = Preference.models.PreferenceAnswer
CustomerPreferenceAnswer = Preference.models.CustomerPreferenceAnswer



def populate_preferences():

    genderQues = PreferenceQuestion.objects.create(
        question="Do you have any gender preference regarding the passenger who sits next to you?",
        description="Gender",
        type=PreferenceQuestion.DROP_DOWN)

    sameSex = PreferenceAnswer.objects.create(preference_question=genderQues, answer='same sex')
    noPreference = PreferenceAnswer.objects.create(preference_question=genderQues, answer='No preference')

    covidSOPQues = PreferenceQuestion.objects.create(
        question="Do you strictly follow Covid SOPs (Masks and sanitizers)?",
        description="Covid SOPs",
        type=PreferenceQuestion.BOOL)
    yes = PreferenceAnswer.objects.create(preference_question=covidSOPQues, answer='Yes')
    no = PreferenceAnswer.objects.create(preference_question=covidSOPQues, answer='No')

    sittingPrefQues = PreferenceQuestion.objects.create(question="Who do you not prefer to sit with?",
                                                        description="sitting",
                                                        type=PreferenceQuestion.CHECK)
    ChattyPeople = PreferenceAnswer.objects.create(preference_question=sittingPrefQues, answer='Chatty people')
    quietPeople = PreferenceAnswer.objects.create(preference_question=sittingPrefQues, answer='Quiet people')
    Children = PreferenceAnswer.objects.create(preference_question=sittingPrefQues, answer='Children')
    Elderlies = PreferenceAnswer.objects.create(preference_question=sittingPrefQues, answer='Elderlies')

    # customer_1 = Customer.objects.get_or_create(username='c1')
    # customer_2 = Customer.objects.create(username='o2', community_score=1.0)
    # customer_3 = Customer.objects.create(username='o3', community_score=1.0)

    # cpa_1 = CustomerPreferenceAnswer.objects.create(customer=customer_1)
    # cpa_1.preference_answers.add(male)


