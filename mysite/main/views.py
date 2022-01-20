from django.shortcuts import render
from django.utils.encoding import smart_text
import dizge
import nltk
import pandas as pd
import datetime

nltk.download('punkt')


# Create your views here.
def index(response):
    return render(response, "main/base.html", {})


def home(response):
    global file_name
    g2p = ''
    syllableCount = ''
    harmony = ''
    syllable_o = ''
    syllable_p = ''
    error2 = ''
    if response.method == 'POST':
        get_text = response.POST.get('text')
        if get_text == '':
            error = 'HATA: Lütfen bir sözcük giriniz'
            error2 = ''.join(error)
        if response.POST.get('submit'):
            checkbox = response.POST.getlist('checkbox')
            print(checkbox)
            for i in checkbox:
                if 'g2p' in i:
                    final = dizge.g2p(get_text)
                    g2p = ''.join(final)
                if 'syllableCount' in i:
                    final = dizge.countSyllable(get_text)
                    print(final)
                    syllableCount = ''.join(str(final))
                if 'harmony' in i:
                    final = dizge.vowelHarmony(get_text)
                    print(final)
                    harmony = ''.join(str(final))
                if 'syllableH' in i:
                    final = dizge.syllable_o(get_text)
                    print(final)
                    syllable_o = ''.join(str(final))
                if 'syllableM' in i:
                    final = dizge.syllable_p(get_text)
                    print(final)
                    syllable_p = ''.join(str(final))

    result_tocsv = []
    g2p_tocsv = []
    syllableCount_tocsv = []
    harmony_tocsv = []
    syllable_o_tocsv = []
    syllable_p_tocsv = []
    # file_name = datetime.datetime.now().strftime('%d%m%y%H%M%S') + '.txt'
    file_name = datetime.datetime.now().strftime('%d%m%y%H%M%S') + '.txt'
    if response.method == 'POST' and 'upload' in response.FILES:
        # uploaded_file = smart_text(response.FILES['upload'].read())
        data = smart_text(response.FILES['upload'].read())
        words = dizge.standardize(data)
        result = dizge.analyze(words, response.POST.getlist('checkboxfile'))
        file = open('results/' + file_name, 'wt', encoding='utf-8')  # '~/home/atagun/PycharmProjects/dizge-web/mysite
        # /results/' +
        output = str(result)
        file.write(output)
        if str(response.FILES['upload']).endswith('.txt'):
            uploaded_file = response.FILES['upload'].read()
            tokens = dizge.standardize(uploaded_file)
            if response.POST.get('submitandprocess'):
                checkbox = response.POST.getlist('checkboxfile')
                result = dizge.analyze(tokens, checkbox)
                file = open('results.txt', 'wt', encoding='utf-8')
                output = str(result)
                file.write(output)
        elif str(response.FILES['upload']).endswith('.csv'):
            pass
        else:
            print('Desteklenmeyen dosya biçimi')

        # ------------------------------------------
        # uploaded_file = pd.read_csv(response.FILES['upload'], sep=";")
        # tokens = uploaded_file
        # for i in tokens:
        #     results = dizge.standardize(i)
        #     result_tocsv.append(results)
        #     for j in results:
        #         if response.POST.get('submitandprocess'):
        #             checkbox = response.POST.getlist('checkboxfile')
        #             for k in checkbox:
        #                 if 'g2p' in k:
        #                     final = dizge.g2p(j)
        #                     g2p_tocsv.append(final)
        #                 if 'syllableCount' in k:
        #                     final = dizge.countSyllable(j)
        #                     syllableCount_tocsv.append(final)
        #                 if 'harmony' in k:
        #                     final = dizge.vowelHarmony(j)
        #                     harmony_tocsv.append(final)
        #                 if 'syllableH' in k:
        #                     final = dizge.syllable_o(j)
        #                     syllable_o_tocsv.append(final)
        #                 if 'syllableM' in k:
        #                     final = dizge.syllable_p(j)
        #                     syllable_p_tocsv.append(final)
    dict_file = {
        'word': result_tocsv,
        'g2p': g2p_tocsv,
        'syllableCount': syllableCount_tocsv,
        'harmony': harmony_tocsv,
        'syllableH': syllable_o_tocsv,
        'syllableM': syllable_p_tocsv,
    }

    df = pd.DataFrame({key: pd.Series(value) for key, value in dict_file.items()})
    df.to_csv('testset.csv', sep=';')
    get_text = response.POST.get('text')
    context = {

    }
    if response.method == 'POST' and get_text != '':
        if response.POST.get('submit'):
            checkbox = response.POST.getlist('checkbox')
            for k in checkbox:
                if 'g2p' in k:
                    context['g2p'] = 'Fonetik Yaz (G2P): ' + str(g2p)
                if 'harmony' in k:
                    context['harmony'] = 'Ünlü Uyumu: ' + str(harmony)
                if 'syllableH' in k:
                    context['syllable_o'] = 'Seslemlere Ayır: ' + str(syllable_o)
                if 'syllableM' in k:
                    context['syllable_p'] = 'Seslemlere Ayır (Dönüştürür): ' + str(syllable_p)
                if 'syllableCount' in k:
                    context['syllableCount'] = 'Seslem Örüntülerini Say: ' + str(syllableCount)
        if response.POST.get('submitandprocess'):
            context['download_link'] = 'results/' + file_name
            context['download_text'] = 'Sonuçları indirmek için tıklayınız!'

    else:
        context = {
            'error2': error2,
        }
    return render(response, 'main/home.html', context)
