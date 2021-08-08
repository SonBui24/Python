def body_mass_index(m, h):
    bmi = m / (h * 2)
    return bmi

def bmi_infomation(body_mass_index):
    if body_mass_index < 18.5:
        print(f'BMI: {body_mass_index} - Gầy')
    elif 18.5 < body_mass_index < 24.9:
        print(f'BMI: {body_mass_index} - Bình thường')
    elif 25 < body_mass_index < 29.9:
        print(f'BMI: {body_mass_index} - Hơi béo')
    elif 30 < body_mass_index < 34.9:
        print(f'BMI: {body_mass_index} - Béo phì cấp 1')
    elif 35 < body_mass_index < 39.9:
        print(f'BMI: {body_mass_index} - Béo phì cấp 2')
    else:
        print(f'BMI: {body_mass_index} - Béo phì cấp 3')

