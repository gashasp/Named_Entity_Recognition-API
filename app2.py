#PUNYA DF

from flask import Flask,render_template,url_for,request, jsonify
import re
import pandas as pd
import spacy
from spacy import displacy
import en_core_web_md
import json 

# @TASK : Load model bahasa 
nlp = en_core_web_md.load()
# END OF TASK 

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process',methods=["POST"])
def process():
    if request.method == 'POST':
        choice = request.form['taskoption']
        rawtext = request.form['rawtext']
        doc2 = nlp(rawtext)
        d2 = []
        if len(doc2.ents) > 0:
            for ent in doc2.ents:
                d2.append((ent.label_, ent.text))
                df2 = pd.DataFrame(d2, columns=['category', 'value'])

                # @TASK : COMPLETE THE FOLLOWING CODES
                ORG_named_entity = df2[df2["category"] == "ORG"]["value"] # Subset semua entitas dengan kategori 'ORG'
                PERSON_named_entity = df2[df2["category"] == "PERSON"]["value"] # Subset semua entitas dengan kategori 'PERSON'
                GPE_named_entity = df2[df2["category"] == "GPE"]["value"] # Subset semua entitas dengan kategori 'GPE'
                MONEY_named_entity = df2[df2["category"] == "MONEY"]["value"] # Subset semua entitas dengan kategori 'MONEY'
                NORP_named_entity = df2[df2["category"] == "NORP"]["value"]
                FAC_named_entity = df2[df2["category"] == "FAC"]["value"]
                LOC_named_entity = df2[df2["category"] == "LOC"]["value"]
                PRODUCT_named_entity = df2[df2["category"] == "PRODUCT"]["value"]
                EVENT_named_entity = df2[df2["category"] == "EVENT"]["value"]
                WORK_OF_ART_named_entity = df2[df2["category"] == "WORK_OF_ART"]["value"]
                LAW_named_entity = df2[df2["category"] == "LAW"]["value"]
                LANGUAGE_named_entity = df2[df2["category"] == "LANGUAGE"]["value"]
                DATE_named_entity = df2[df2["category"] == "DATE"]["value"]
                TIME_named_entity = df2[df2["category"] == "TIME"]["value"]
                QUANTITY_named_entity = df2[df2["category"] == "QUANTITY"]["value"]
                ORDINAL_named_entity = df2[df2["category"] == "ORDINAL"]["value"]
                CARDINAL_named_entity = df2[df2["category"] == "CARDINAL"]["value"]
                # END OF TASK 

            if choice == 'organization':
                results = ORG_named_entity
                num_of_results = len(results)
            elif choice == 'person':
                results = PERSON_named_entity
                num_of_results = len(results)
            elif choice == 'geopolitical':
                results = GPE_named_entity
                num_of_results = len(results)
            elif choice == 'money':
                results = MONEY_named_entity
                num_of_results = len(results)
            elif choice == 'norp':
                results = NORP_named_entity
                num_of_results = len(results)
            elif choice == 'fac':
                results = FAC_named_entity
                num_of_results = len(results)
            elif choice == 'loc':
                results = LOC_named_entity
                num_of_results = len(results)
            elif choice == 'product':
                results = PRODUCT_named_entity
                num_of_results = len(results)
            elif choice == 'event':
                results = EVENT_named_entity
                num_of_results = len(results)
            elif choice == 'work_of_art':
                results = WORK_OF_ART_named_entity
                num_of_results = len(results)
            elif choice == 'law':
                results = LAW_named_entity
                num_of_results = len(results)
            elif choice == 'language':
                results = LANGUAGE_named_entity
                num_of_results = len(results)
            elif choice == 'date':
                results = DATE_named_entity
                num_of_results = len(results)
            elif choice == 'time':
                results = TIME_named_entity
                num_of_results = len(results)
            elif choice == 'quantity':
                results = QUANTITY_named_entity
                num_of_results = len(results)
            elif choice == 'ordinal':
                results = ORDINAL_named_entity
                num_of_results = len(results)
            elif choice == 'cardinal':
                results = CARDINAL_named_entity
                num_of_results = len(results)

        else:
            results = pd.DataFrame()
            num_of_results = len(results)

    return render_template("index.html",results=results,num_of_results = num_of_results, original_text = rawtext)

@app.route('/endpoint_tertentu')
def nama_fungsi_tertentu():
    # secara teknis, kita dapat melakukan apapun dalam fungsi ini 
    return ("Fungsi ini akan dijalankan saat endpoint tersebut diakses")

@app.route('/endpoint_get', methods=['GET'])
def contoh_get():
    return ("Contoh endpoint get")

@app.route('/endpoint_post', methods=['POST'])
def contoh_post():
    return ("Contoh endpoint post")

@app.route('/endpoint_multi', methods=['GET', 'POST'])
def multi_method():
    if request.method == 'POST':
        return ("Nilai ini akan dikembalikan jika endpoint ini diakses dengan method POST")
    else : 
        return ("Nilai ini akan dikembalikan jika endpoint ini diakses dengan method GET")

@app.route('/tes_send_json', methods=['POST'])
def tes_send_json():
    data = request.get_json() # proses membaca json yang dikirim 
    nama = data['nama']
    usia = data['usia']
    pekerjaan = data['pekerjaan']

    return ("Halo, {nama}. Usiamu adalah {usia} dan pekerjaanmu adalah {pekerjaan}".format(nama=nama, usia=usia, pekerjaan=pekerjaan))

@app.route('/tes_return_json', methods=['POST'])
def tes_return_json():
    data = request.get_json() # proses membaca json yang dikirim 
    df = pd.DataFrame([data]) # mengolah data menjadi dataframe

    return (df.to_json()) # mengembalikan dataframe dalam bentuk json

@app.route('/get_entities', methods=['POST'])
def get_entities():
    
    # ambil data dari json yang diterima endpoint
    data3 = request.get_json()
    
    # ambil nilai teks dari data
    text3 = data3['text3']
    
    # modelkan teks dengan model spacy 
    doc3 = nlp(text3)
    
    # membuat pasangan label dan nilai entitas
    d3 = [(ent.label_, ent.text) for ent in doc3.ents]

    # transform pasangan label menjadi dataframe 
    df3 = pd.DataFrame(d3, columns=['category', 'value'])
    
    return (df3.to_json())

if __name__ == '__main__':
    app.run(debug=True)
