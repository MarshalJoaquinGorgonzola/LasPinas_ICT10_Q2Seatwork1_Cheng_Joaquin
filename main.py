from pyscript import document 

def candidate_checker(e): 
    club_members = ['juan delacruz', 'two delacruz', 
    'three delacruz', 'four delacruz', 
    'five delacruz', 'six delacruz', 
    'seven delacruz', 'eight delacruz', 
    'nine delacruz', 'ten delacruz']
    f_name = document.getElementById('first_name').value
    l_name = document.getElementById('last_name').value
    candidate = f_name + '' + l_name
    member_checker = candidate.lower() in club_members

    messages = (f'Sorry {candidate}, your name is not on the list.',
     f'Congratulations {candidate}! You are part of the ICT Club.')

    document.getElementById('result').innerHTML=messages[member_checker]
