cities = {
	'silvis': {
	'country': 'USA',
	'population': 7537,
	'fact': 'Silvis is a city in Rock Island County, Illinois, United States.'\
	' It is part of a larger metropolitan area known as the Quad Cities. The'\
	' Quad Cities Metropolitan Area is situated across four counties in'\
	' Illinois and Iowa and Brandie was born here.'
	},
	'detroit': {
	'country': 'USA',
	'population': 672662,
	'fact': 'Detroit is the largest city in the midwestern state of Michigan.'\
	' Near Downtown, the neoclassical Detroit Institute of Arts is famed for '\
	'the Detroit Industry Murals painted by Diego Rivera, and inspired by the'\
	" city's ties to the auto industry, giving it the nickname 'Motor City.' "\
	'Detroit is also the birthplace of Motown Records, whose chart-topping'\
	' history is on display at their original headquarters, Hitsville U.S.A.'
	},
	'indianapolis': {
	'country': 'USA',
	'population': 876862,
	'fact': 'Indianapolis, often shortened to Indy, is the state capital and'\
	' most-populous city of the U.S. state of Indiana and the seat of Marion'\
	' County. According to 2019 estimates from the U.S. Census Bureau, the'\
	' consolidated population of Indianapolis and Marion County was 886,220.'
	},

}

for city, info in cities.items():
	print(f"\n{city.upper()}")
	print(f"\tPopulation: {info['population']}")
	print(f"\tCountry: {info['country']}")
	print(f"\tFun Fact: {info['fact']}")
