
# Definir las probabilidades condicionales de los sintomas dado covid-19
p_fatiga_given_covid = 0.80
p_tos_seca_given_covid = 0.90
p_dificultad_respirar_given_covid = 0.30
p_dolor_garganta_given_covid = 0.40
p_dolor_cabeza_given_covid = 0.50
p_dolor_cuerpo_given_covid = 0.70
p_escalofrios_given_covid = 0.60
p_secrecion_nasal_given_covid = 0.90
p_perdida_sentido_given_covid = 0.80
p_fiebre_given_covid = 0.90
p_dolor_pecho_given_covid = 0.70
# Definir la prevalencia de covid en la poblacion
p_covid = 0.05
# Definir los sintomas observados en el paciente
sintomas = ['Fatiga','Tos seca','Dificultad para respirar','Dolor de garganta', 
            'Dolor de cabeza', 'Dolor en el cuerpo', 'Escalofrios', 'Secrecion nasal',
            'Perdida del sentido del olfato o del gusto', 'Fiebre', 'Dolor de pecho']
# Calcular la probabilidad de que el paciente tenga covid
p_sintomas_given_covid = p_fatiga_given_covid * p_tos_seca_given_covid * p_dificultad_respirar_given_covid * \
                         p_dolor_garganta_given_covid * p_dolor_cabeza_given_covid * p_dolor_cuerpo_given_covid * \
                         p_escalofrios_given_covid * p_secrecion_nasal_given_covid * p_perdida_sentido_given_covid *\
                         p_fiebre_given_covid * p_dolor_pecho_given_covid
p_sintomas_given_no_covid = 0.05 ** 11 # se asume que la porbabilidad de tener los sintomas es baja
p_covid = 0.05
p_sintomas = p_sintomas_given_covid * p_covid + p_sintomas_given_no_covid * (1 - p_covid)
p_covid_given_sintomas = p_sintomas_given_covid * p_covid / p_sintomas
print(f"la probabilidad de que el paciente tenga COVID-19 dados los sintomas es: {p_covid_given_sintomas}")
