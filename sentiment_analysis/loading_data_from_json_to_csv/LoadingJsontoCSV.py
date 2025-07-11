# Changing pwd to my working directory
# use if required
#cd A:\Project\New_data\tweets

#loading all the json files from a text file and loading tweet data onto a list
import json
import csv

whole_data = []
file = open('filename.txt')
lines = file.readlines()
for eachline in lines:
    eachline = eachline.strip('\n')
    print(eachline)
    f = open(eachline)
    json_file = json.load(f)
    whole_data.append(json_file)
    f.close()
file.close()

#creating keys and keys1 as lists
# Those are the fields I needed for my project and needs to be extracted from the JSON files 

keys = ['created_at', 'screen_name','id', 'in_reply_to_status_id_str', 'hashtags','truncated', 'location', 'followers_count','favorite_count','retweet_count','reply_count', 'possibly_sensitive', 'lang','text']
keys1 = ['created_at', 'screen_name','id', 'in_reply_to_status_id_str', 'hashtags','truncated', 'location', 'followers_count','favorite_count','retweet_count','reply_count', 'possibly_sensitive', 'lang', 'full_text']

#extracting required fields from the JSON files and loading it to a CSV
with open('filename.csv', 'a+', encoding ='UTF8') as f:
    writer = csv.DictWriter(f, fieldnames = keys)
    for x in range(len(whole_data)):
        whole_data1 = dict(whole_data[x])
        new_dic = {}
        for i in range(len(keys)):
            #print(i)
            if whole_data1['truncated']== False:
                try:
                    try:
                        if i == 2 or i ==3:
                            new_dic[keys[i]] = ('\'',whole_data1[keys[i]],'\'')
                        else:                        
                            new_dic[keys[i]] = whole_data1[keys[i]]
                    except:
                        try:
                            new_dic[keys[i]] = whole_data1['user'][keys[i]]
                        except:
                            new_dic[keys[i]] = whole_data1['entities'][keys[i]]
                            try:
                                new_dic[keys[i]] = ''
                            except:
                                continue
                except:
                    continue
            elif whole_data1['truncated']== True:
                try:
                    try:
                        try:
                            if i == 2 or i ==3:
                                new_dic[keys1[i]] = ('\'',whole_data1[keys1[i]],'\'')
                            else:                        
                                new_dic[keys1[i]] = whole_data1[keys1[i]]
                        except:
                            try:
                                new_dic[keys1[i]] = whole_data1['user'][keys1[i]]
                            except:
                                new_dic[keys1[i]] = whole_data1['entities'][keys1[i]]
                    except:
                        try:
                            new_dic['text'] = whole_data1['extended_tweet'][keys1[i]]
                        except:
                            new_dic[keys1[i]] = ''
                except:
                    continue
        writer.writerow(new_dic)
                
             
        
    
    
