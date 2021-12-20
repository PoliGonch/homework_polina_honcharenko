def make_country(country_name: str, capital_name: str) -> dict[str, str]:
    country_dict = {'name': country_name, 'capital': capital_name}
    print(f'Country: {country_dict.get("name")}, Capital: {country_dict.get("capital")}')
    return country_dict


make_country(country_name='USA', capital_name='Washington')
