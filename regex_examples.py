import re

phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('Hello call 999-888-7777 or 333-666-5555 for emeregencies')

print(mo.group(2))

bat_regex = re.compile(r'bat(man|mobile|bat)')
# mo_bat = bat_regex.search('can i rent a batmobile?')
mo_bat = bat_regex.search('can i rent a batbike?')

# print(mo_bat.group())
print(mo_bat == None)

spider_regex = re.compile(r'spider(wo)?man') #'?' character means (wo) can appear zero or one time

mo_spider = spider_regex.search('The amazing spiderwoman')
print(mo_spider.group())

phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo_phone = phone_regex.search('Call me at 999-9898')
print(mo_phone.group())

super_regex = re.compile(r'super(wo)*man') #'*' character means (wo) can appear zero or more times
mo_super = super_regex.search("The superwowowowowowowowowowoman movie")
print(mo_super.group())

bat_regex_1 =  re.compile(r'bat(wo)+man') #(+) character means (wo) can appear one or more times 
mo_bat_1 = bat_regex_1.search('The adventures of batwowowoman')
print(mo_bat_1.group())

ha_regex = re.compile(r'(ha){3}') # '{x} notation means that the group of string needs to appear exactly x no. of times
mo_ha = ha_regex.search('All I heard was hahaha')
print(mo_ha.group())

phone_regex_1 = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo_phone_1 = phone_regex_1.search('My numbers are 999-888-9999,888-777-5555,555-6666')
print(mo_phone_1.group())

ha_regex_1 = re.compile(r'(ha){2,5}') # '{x,y} notation means that the group of string needs to appear at least x times and at most y times
mo_ha_1 = ha_regex_1.search('All I heard was hahahaha')
print(mo_ha_1.group())


digit_regex = re.compile(r'(\d){3,5}') #python does greedy search. hence searches for the most numbers possible
mo_digit = digit_regex.search('123456789')
print(mo_digit.group())

digit_regex_1 = re.compile(r'(\d){3,5}?') #{}? notation is used for performing non greedy searches. i.e. searches for the least numbers possible
mo_digit_1 = digit_regex_1.search('123456789')
print(mo_digit_1.group())

find_all_regex = re.compile('\d\d\d-\d\d\d-\d\d\d\d')
resume = 'The numbers in this resume are 999-888-7777, 888-777-5555, 666-666-4444'
num_list = find_all_regex.findall(resume) #findall returns list of matched values instead of match objects
print(num_list)

find_all_regex_1 = re.compile('(\d\d\d)-(\d\d\d-\d\d\d\d)')
resume = 'The numbers in this resume are 999-888-7777, 888-777-5555, 666-666-4444'
num_list_1 = find_all_regex_1.findall(resume) #findall returns list of matched values instead of match objects
print(num_list_1)

begins_with_hello_regex = re.compile(r'^Hello') 
mo_hello = begins_with_hello_regex.search('Hello World')
print(mo_hello.group())

all_digits_regex = re.compile(r'^\d+$')
mo_all_digits = all_digits_regex.search('123165484956654')
print(mo_all_digits.group())

at_regex = re.compile(r'.{1,2}at')
mo_at = at_regex.findall('The cat with the hat sat on the flat mat')
print(mo_at)

name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
print(name_regex.findall('First Name: John Last Name: Silva'))



serve = '<To serve humans> for dinner>'

nongreedy_regex = re.compile(r'<(.*?)>') #.*? for non greedy search
print(nongreedy_regex.findall(serve))

greedy_regex = re.compile(r'<(.*)>') #.* for greedy search
print(greedy_regex.findall(serve))

prime = 'Serve the public trust.\nProtect the Innocent.\nUpload the law'
dotall_regex = re.compile(r'.*', re.DOTALL) #passing re.DOTALL includes even the new lines
print(dotall_regex.search(prime).group())

vowel_regex = re.compile(r'[aeiou]', re.IGNORECASE) #re.IGNORECASE for case insensitive searching
print(vowel_regex.findall('AEIOU'))

agent_regex = re.compile(r'Agent \w+')
print(agent_regex.findall('Agent John gave the documents to Agent Cena'))
print(agent_regex.sub('REDACTED','Agent John gave the documents to Agent Cena'))

agent_regex_1 = re.compile(r'Agent (\w)\w*')
print(agent_regex_1.findall('Agent John gave the documents to Agent Cena'))
print(agent_regex_1.sub(r'Agent \1****','Agent John gave the documents to Agent Cena'))

verbose_regex = re.compile(r'''
\d\d\d #verbose mode allows adding comments, spaces and new lines without them being part of the regular expression
-
\d\d\d
-
\d\d\d\d
''', re.VERBOSE)

multiple_regex_config = re.compile(r'\d+', re.DOTALL | re.IGNORECASE | re.VERBOSE) # | (Bit wise OR operator allows passing multiple config parameters into the compile function)