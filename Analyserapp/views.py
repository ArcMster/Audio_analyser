from __future__ import print_function
from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from .models import Input_audios, Output_audios
import pandas as pd
import numpy as np
import time, datetime
import librosa
import librosa.display
from sklearn.metrics import mean_squared_error
from sklearn.metrics import max_error
import matplotlib.pyplot as plt
from pydub import AudioSegment
from pydub.playback import play
import wave
import os
from django.http import HttpResponse


# Create your views here.

def home(request):
    return render(request,'home.html')



def file_upload(request):
    input_file = Input_audios()
    '''if request.method == 'POST':
        upload_file = request.FILES['audio1']
        print(upload_file.name)
        print(upload_file.size)'''

    #file1 = request.POST['audio1']
    file1 = request.FILES['audio1']
    file2 = request.FILES['audio2']
    file3 = request.FILES['audio3']
    file_analyse = request.FILES['analyse']
    


    input_file.audio_1 = file1
    input_file.audio_2 = file2
    input_file.audio_3 = file3
    input_file.audio_analyse = file_analyse
    input_file.save()
    obj = Input_audios.objects.last()
    print("started")
    audio1 = "C:\\Users\\PSSRE\\Djangoproject\\Freelance\\Audio_project\\Audio_analyser\\media\\media\\" + str(obj.audio_1)[5:]
    audio2 = "C:\\Users\\PSSRE\\Djangoproject\\Freelance\\Audio_project\\Audio_analyser\\media\\media\\" + str(obj.audio_2)[5:]
    audio3 = "C:\\Users\\PSSRE\\Djangoproject\\Freelance\\Audio_project\\Audio_analyser\\media\\media\\" + str(obj.audio_3)[5:]
    audioanalyse = "C:\\Users\\PSSRE\\Djangoproject\\Freelance\\Audio_project\\Audio_analyser\\media\\media\\" + str(obj.audio_analyse)[5:]
    print("a")

    search_function(keyword_file1= audio1, keyword_file2=audio2, keyword_file3 = audio3,
                    large_audio_file=audioanalyse)
    
    output_files = Output_audios.objects.last()
    return render(request,'audio_results.html',{'audio': output_files},{'inaudio':obj})
'''
    new_file = Output_audios()
    new_file.search_1 = audio_output[0]
    print(audio_output[0])
    new_file.search_2 = audio_output[1]
    new_file.search_3 = audio_output[2]
    new_file.search_4 = audio_output[3]
    new_file.search_5 = audio_output[4]
    new_file.search_6 = audio_output[5]
    print("i")

    outfile = Output_audios.objects.last()

    return render(request,'results.html',{'audio':outfile})
'''
'''
    print(new_file.search_2)

    new_file.save()

    all_audio = []
    audio_files = Input_audios.objects.all()


    for i in audio_files:
        all_audio.append(i)

    return render(request,'results.html',{'audios':all_audio})
'''


    

    
    



def result_page(request):
    audio_files = Input_audios.objects.all()

    all_audio = []
    for i in audio_files:
        all_audio.append(i)

    return render(request,'results.html',{'audios':all_audio})


"================================================"

def get_chroma_features(sound_window = [], plot=True):
    y = sound_window
    
    # Compute chroma features from the harmonic signal
    chroma_cq = librosa.feature.chroma_cqt(y=y,
                                       sr=22050, hop_length= 512)
    
    if plot == True:
        
        librosa.display.specshow(chroma_cq, y_axis='chroma', x_axis='time')
        plt.title('chroma_cqt')
        plt.colorbar()       
        plt.tight_layout()
        plt.show()

        for pitch_class in range(0,12):

            title_str = "Pitch Class: " + str(pitch_class)
            plt.figure(figsize=(17,5))
            plt.title(title_str)
            plt.plot(chroma_cq[pitch_class,:])
            plt.show()
    
    df1 = pd.DataFrame(chroma_cq).T.add_prefix('pitch_')
    
    return df1



def get_mel_spectrogram_features(sound_window = [], plot= True):       
    # rename window
    y = sound_window
    
    mel_spec = librosa.feature.melspectrogram(y=y, sr=22050)
    
    if plot == True:
        
        librosa.display.specshow(mel_spec, x_axis='time',y_axis='mel', sr=sr,fmax=8000)
        plt.colorbar(format='%+2.0f dB')
        plt.title('Mel-frequency spectrogram')
        plt.tight_layout()
        plt.show()

        for freq in range(0,128):

            title_str = "Mel Class: " + str(freq)
            plt.figure(figsize=(17,5))
            plt.title(title_str)
            plt.plot(mel_spec[freq,:])
            plt.show()
    
    df1 = round(pd.DataFrame(mel_spec).T.add_prefix('mel_'),6)
    
    df2 = df1[['mel_0', 'mel_1', 'mel_2', 'mel_3', 'mel_4', 'mel_5', 'mel_6', 'mel_7',
       'mel_8', 'mel_9', 'mel_10', 'mel_11', 'mel_12', 'mel_13', 'mel_14',
       'mel_15', 'mel_16', 'mel_17', 'mel_18', 'mel_19', 'mel_20', 'mel_21',
       'mel_22', 'mel_23', 'mel_24', 'mel_25', 'mel_26', 'mel_27', 'mel_28',
       'mel_29', 'mel_30', 'mel_31', 'mel_32', 'mel_33', 'mel_34', 'mel_35',
       'mel_36', 'mel_37', 'mel_38', 'mel_39', 'mel_40', 'mel_41', 'mel_42',
       'mel_43', 'mel_44', 'mel_45', 'mel_46', 'mel_47', 'mel_48', 'mel_49',
       'mel_50', 'mel_51', 'mel_52', 'mel_53', 'mel_54', 'mel_55', 'mel_56',
       'mel_57', 'mel_58', 'mel_59', 'mel_60', 'mel_61', 'mel_62', 'mel_63',
       'mel_64', 'mel_65', 'mel_66', 'mel_67', 'mel_68', 'mel_69', 'mel_70',
       'mel_71', 'mel_72', 'mel_73', 'mel_74', 'mel_75', 'mel_76', 'mel_77',
       'mel_78', 'mel_79', 'mel_80', 'mel_81', 'mel_82', 'mel_83', 'mel_84',
       'mel_85', 'mel_86', 'mel_87', 'mel_88', 'mel_89', 'mel_90', 'mel_91',
       'mel_92', 'mel_93', 'mel_94', 'mel_95', 'mel_96', 'mel_97']]
    
    
    return df2


# target_audio, target_sr = librosa.load('Voice_042.wav')
#
    # len(target_audio)
# yt, index = librosa.effects.trim(target_audio, top_db=40)
# len(yt)
# mf_table = get_mel_spectrogram_features(sound_window = yt, plot= False)
# mf_table.describe().T.sort_values(by='50%', ascending=False)
# mf_table.describe().T.loc[~(mf_table.describe().T['50%'] == 0)].index



def get_zero_crossing_rate(sound_window = [], plot=True):
    
    # rename window
    y = sound_window
    
    cross_rate = librosa.feature.zero_crossing_rate(y=y)
    
    if plot == True:
        title_str = "Zero Crossing Rate"
        plt.figure(figsize=(17,5))
        plt.title(title_str)
        plt.plot(cross_rate[0,:])
        plt.show()
    
    df1 = pd.DataFrame(cross_rate).T.rename(columns={0:'Zero_Cross_Rate'})
    
    return df1


def get_features(sound_window = [], feature_name = 'chroma'):
    
    if feature_name == 'chroma':
        # get chroma features
        feature_df = get_chroma_features(sound_window = sound_window, plot=False)
        
    elif feature_name == 'melspec':
        # get mel spectrogram features
        feature_df = get_mel_spectrogram_features(sound_window = sound_window, plot=False)
    
    elif feature_name == 'zerocross':
        # get zero crossing rate
        feature_df = get_zero_crossing_rate(sound_window = sound_window, plot=False)
    
    # merge the dataframe
#     comb_df1 = pd.merge(chroma_cq_df, mel_spec_df, left_index= True, right_index=True, how='inner')
#     comb_df2 = pd.merge(comb_df1, zero_cross_df, left_index= True, right_index=True, how='inner')
    
#     print(comb_df2.shape)
    
    return feature_df



def compare_features(test_audio = [], target_audio = [], feature_name='melspec', plot=True):       
    start_time_seconds = time.time()
    
    window_size = len(target_audio)
    rmse_holder = []
    max_error_holder = []
    sample_holder = []
    # get features for the target audio
    feature_target = get_features(sound_window = target_audio, feature_name= feature_name)
    
    for i in range(0, len(test_audio), window_size):
        
        test_set = test_audio[i:i+window_size]
        
        if len(test_set) == window_size:
            
            feature_test = get_features(sound_window = test_set, feature_name= feature_name)
            
            # calculate the rmse
            rmse = mean_squared_error(feature_target, feature_test, squared=False)
            rmse_holder.append(rmse)
            # calculate the max error score - on raw audio itself
            max_error_val = max_error(target_audio, test_set)
            max_error_holder.append(max_error_val)
            # append the sample holder
            sample_holder.append(i)
            
        elif len(test_set) < window_size:
            
            last_test_set = test_audio[-window_size:]
            
            feature_test = get_features(sound_window = last_test_set, feature_name= feature_name)
            
            # calculate the rmse
            rmse = mean_squared_error(feature_target, feature_test, squared=False)
            rmse_holder.append(rmse)
            # calculate the max error score - on raw audio itself
            max_error_val = max_error(target_audio, last_test_set)
            max_error_holder.append(max_error_val)
            # append the sample holder
            sample_holder.append(i)
            
        
    if plot == True:
        plt.figure(figsize=(17,5))
        plt.title('RMSE Graph')
        plt.plot(rmse_holder, color='teal');
        plt.show()
        plt.figure(figsize=(17,5))
        plt.title('Max Error Graph')
        plt.plot(max_error_holder, color='darkgoldenrod');
        plt.show()
        
    result_df = pd.DataFrame({'sample_loc': sample_holder, 'rmse': rmse_holder, 'max_error': max_error_holder})
    
    stop_time_seconds = time.time()
    runtime = round((stop_time_seconds - start_time_seconds),2)
    print('The feature extraction and comparison runtime of ', feature_name, ' is: ', runtime, ' seconds')
    return result_df, runtime


def cost_function(featureList=['melspec', 'chroma', 'zerocross'], coefficientValues= [0.9, 0.9, 0.8],
                  target_audio = [], test_audio=[], plot=True):
    print("d")
    
    # TODO -- iterate over the feature list and add results in the placeholder
    
    # when the feature name is melspec
    result_melspec, runtime_melspec = compare_features(test_audio = test_audio, target_audio = target_audio,
                                                       feature_name='melspec', plot=False)
    # when the feature name is melspec
    result_chroma, runtime_chroma = compare_features(test_audio = test_audio, target_audio = target_audio,
                                                       feature_name='chroma', plot=False)
    # when the feature name is melspec
    result_zerocross, runtime_zerocross = compare_features(test_audio = test_audio, target_audio = target_audio,
                                                       feature_name='zerocross', plot=False)
    
    # set index of result df at sample loc
    result_melspec2 = result_melspec.set_index('sample_loc')
    result_chroma2 = result_chroma.set_index('sample_loc')
    result_zerocross2 = result_zerocross.set_index('sample_loc')
    
    # set coefficients for each
    agg_df = result_melspec2 * coefficientValues[0] + result_chroma2 * coefficientValues[1] + \
                result_zerocross2 * coefficientValues[2]
    
    avg_df = agg_df / len(featureList)
    
    
    if plot == True:
        plt.figure(figsize=(17,5))
        plt.title('RMSE Graph')
        plt.plot(avg_df['rmse'], color='teal');
        plt.show()
        plt.figure(figsize=(17,5))
        plt.title('Max Error Graph')
        plt.plot(avg_df['max_error'], color='darkgoldenrod');
        plt.show()
    
    return avg_df


def evaluate_comparison(result_df = pd.DataFrame(), rmse_threshold = 10, max_error_threshold = 0.20):
    print("e")
    
    result_df = result_df.reset_index()
    # sort the result with min rmse and max error
    sorted_df = result_df.sort_values(by=['rmse', 'max_error'], ascending=[True, True])
    
    # find the sample loc of the min rmse and min of max error
    start_loc = sorted_df['sample_loc'].iloc[0]
    selected_rmse = sorted_df['rmse'].iloc[0]
    selected_max_error = sorted_df['max_error'].iloc[0]
    
    
    # if the rmse and max error are below certain threshold
    if (selected_rmse < rmse_threshold) and (selected_max_error < max_error_threshold):
    
        # Print
        print('The target audio clip has potentially been found')
        print('The target audio starts at: ', start_loc, ' sample')
        print('The RMSE of the sample is : ', selected_rmse)
        print('The Max Error of the sample is : ', selected_max_error)
        
    else:
        print('The target audio clip could not be found')
        
    return sorted_df


def trim_resample_average(sample_1_file='abc.wav', sample_2_file='def.wav', sample_3_file='ghi.wav'):
    print("c")  
    # read the file and get timeseries
    raw_y1, sr1 = librosa.load(sample_1_file, sr= 22050)
    raw_y2, sr2 = librosa.load(sample_2_file, sr= 22050)
    raw_y3, sr3 = librosa.load(sample_3_file, sr= 22050)
    
    # trim the start and end silence
    y1, index1 = librosa.effects.trim(raw_y1, top_db=35)
    y2, index2 = librosa.effects.trim(raw_y2, top_db=35)
    y3, index3 = librosa.effects.trim(raw_y3, top_db=35)
    
    # calculate the mean length of the time series
    avg_length = np.mean([len(y1), len(y2), len(y3)])
    
    # determine the new sampling rate adjusted for the average length
    time_duration_1 = len(y1) / sr1
    new_sr1 = avg_length / time_duration_1
    
    time_duration_2 = len(y2) / sr2
    new_sr2 = avg_length / time_duration_2
    
    time_duration_3 = len(y3) / sr3
    new_sr3 = avg_length / time_duration_3
    
    # resample the audio signals with new sampling rate
    adj_y1 = librosa.resample(y1, sr1, new_sr1)
    adj_y2 = librosa.resample(y2, sr2, new_sr2)
    adj_y3 = librosa.resample(y3, sr3, new_sr3)
    
    # calculate the mean of the adjusted sampling rate
    mean_new_sr = np.mean([new_sr1, new_sr2, new_sr3])
    
    # calculate the mean of three audio time series
    mean_new_y = np.mean([adj_y1, adj_y2, adj_y3], axis=0)
    
    # return mean y and mean sr
    return mean_new_y, mean_new_sr



def write_audio_output(potential_df = pd.DataFrame(), target_length = 10.0, test_audio=[], test_sr=10.0):
    output = Output_audios()
    
    # convert the first search result into audio
    start_point = potential_df['sample_loc'].iloc[0]
    end_point = start_point + target_length
    audio_subset = test_audio[start_point: end_point]

    current_time = datetime.datetime.now()
    timestr = str(current_time.year) + "_" + str(current_time.month) + "_" + str(current_time.day) + "_" + str(current_time.hour) + "_" + str(current_time.minute) + "_" + str(current_time.second)
    timesave = "C:\\Users\\PSSRE\\Djangoproject\\Freelance\\Audio_project\\Audio_analyser\\media\\media\\search_1" + timestr
    librosa.output.write_wav(timesave, audio_subset, sr=test_sr)
    
    output.search_1 = "media/search_1" + timestr
    
    #search = open('C:\\Users\\PSSRE\\Djangoproject\\Freelance\\search_1.wav','r')
    #output_list.append(search)
    
    #audio_output.search_1 = wave.open('C:\\Users\\PSSRE\\Djangoproject\\Freelance\\search_1.wav')
    
    # convert the second search result into audio
    start_point = potential_df['sample_loc'].iloc[1]
    end_point = start_point + target_length
    audio_subset = test_audio[start_point: end_point]
    timesave = "C:\\Users\\PSSRE\\Djangoproject\\Freelance\\Audio_project\\Audio_analyser\\media\\media\\search_2" + timestr
    librosa.output.write_wav(timesave, audio_subset, sr=test_sr)
    output.search_2 = "media/search_2" + timestr
    
    # convert the third search result into audio
    start_point = potential_df['sample_loc'].iloc[2]
    end_point = start_point + target_length
    audio_subset = test_audio[start_point: end_point]
    timesave = "C:\\Users\\PSSRE\\Djangoproject\\Freelance\\Audio_project\\Audio_analyser\\media\\media\\search_3" + timestr
    librosa.output.write_wav(timesave, audio_subset, sr=test_sr)
    output.search_3 = "media/search_3" + timestr
    
    # convert the fourth search result into audio
    start_point = potential_df['sample_loc'].iloc[3]
    end_point = start_point + target_length
    audio_subset = test_audio[start_point: end_point]
    timesave = "C:\\Users\\PSSRE\\Djangoproject\\Freelance\\Audio_project\\Audio_analyser\\media\\media\\search_4" + timestr
    librosa.output.write_wav(timesave, audio_subset, sr=test_sr)
    output.search_4 = "media/search_4" + timestr
    
    # convert the fifth search result into audio
    start_point = potential_df['sample_loc'].iloc[4]
    end_point = start_point + target_length
    audio_subset = test_audio[start_point: end_point]
    timesave = "C:\\Users\\PSSRE\\Djangoproject\\Freelance\\Audio_project\\Audio_analyser\\media\\media\\search_5" + timestr
    librosa.output.write_wav(timesave, audio_subset, sr=test_sr)
    output.search_5 = "media/search_5" + timestr
    
    # convert the fifth search result into audio
    start_point = potential_df['sample_loc'].iloc[5]
    end_point = start_point + target_length
    audio_subset = test_audio[start_point: end_point]
    timesave = "C:\\Users\\PSSRE\\Djangoproject\\Freelance\\Audio_project\\Audio_analyser\\media\\media\\search_6" + timestr
    librosa.output.write_wav(timesave, audio_subset, sr=test_sr)
    output.search_6 = "media/search_6" + timestr
    output.save()
    


def search_function(keyword_file1= 'abc.wav', keyword_file2='def.wav', keyword_file3 = 'ghi.wav',
                    large_audio_file='xyz.wav'):
    
    
    target_audio, target_sr = trim_resample_average(sample_1_file=keyword_file1,
                                                    sample_2_file=keyword_file2, sample_3_file=keyword_file3)
    
    
    target_audio, target_sr = librosa.load(keyword_file1)
    
    target_audio, index = librosa.effects.trim(target_audio, top_db=40)
    
    test_filename = large_audio_file
    
    test_audio, test_sr = librosa.load(test_filename, sr= target_sr)
    
    result = cost_function(featureList=['melspec', 'chroma', 'zerocross'],
                       coefficientValues= [0., 1.2, 0.0], 
                       target_audio = target_audio,
                        test_audio = test_audio,
#                       test_audio=test_audio[int(test_sr*2):-int(test_sr*2)],
                       plot=False)
    
    potential_df = evaluate_comparison(result_df = result, rmse_threshold = 7, max_error_threshold = 0.70)
    
    # store the output in audio form
    file_list = write_audio_output(potential_df = potential_df, target_length = len(target_audio),
                       test_audio=test_audio, test_sr=int(test_sr))
    
    return potential_df, file_list


search_function(keyword_file1= 'C:\\Users\\PSSRE\\Djangoproject\\Freelance\\Voice_042.wav', keyword_file2='C:\\Users\\PSSRE\\Djangoproject\\Freelance\\Voice 043.wav', keyword_file3 = 'C:\\Users\\PSSRE\\Djangoproject\\Freelance\\Voice 044.wav',
                    large_audio_file='C:\\Users\\PSSRE\\Djangoproject\\Freelance\\Voice 045.wav')
