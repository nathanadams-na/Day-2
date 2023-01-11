age = input("How old are you?: \t")
weeks_lived = int(age) * 52
days_lived = weeks_lived * 7
hours_lived = days_lived * 24

weeks_in_90 = 90 * 52
weeks_left = weeks_in_90 - weeks_lived
days_left = weeks_left * 7
hours_left = days_left * 24
print(f"You have Lived {hours_lived} hours, {days_lived} days, {weeks_lived} weeks")
print(f"\nIn the unlikely event you live to 90; \nYou have {hours_left} hours left, {days_left} days left, {weeks_left} weeks left. ")
