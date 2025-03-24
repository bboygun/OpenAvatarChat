import unittest
from funasr import AutoModel
from funasr.utils.postprocess_utils import rich_transcription_postprocess
import numpy as np

import soundfile
import os

if __name__ == '__main__':
    model = AutoModel(
        model='iic/SenseVoiceSmall',
        # vad_model="fsmn-vad",
        # vad_kwargs={"max_single_segment_time": 30000},
        # device="mps",
    )
    chunk_size = [0, 10, 5]  # [0, 10, 5] 600ms, [0, 8, 4] 480ms
    encoder_chunk_look_back = 4  # number of chunks to lookback for encoder self-attention
    decoder_chunk_look_back = 1  # number of encoder chunks to lookback for decoder cross-attention

    wav_file = os.path.join(model.model_path, "example/asr_example.wav")
    speech, sample_rate = soundfile.read(wav_file)
    chunk_stride = chunk_size[1] * 960  # 600ms

    cache = {}
    total_chunk_num = int(len((speech)-1)/chunk_stride+1)
    for i in range(total_chunk_num):
        speech_chunk = speech[i*chunk_stride:(i+1)*chunk_stride]
        is_final = i == total_chunk_num - 1
        res = model.generate(input=speech_chunk, cache=cache, is_final=is_final, chunk_size=chunk_size,
                             encoder_chunk_look_back=encoder_chunk_look_back, decoder_chunk_look_back=decoder_chunk_look_back)
        print(res)
    # data = np.array([ 3.04177970e-01 ,  3.02713096e-01 ,  3.00180048e-01 ,  2.80373544e-01 ,   2.53700376e-01 ,  2.24524677e-01 ,  1.88604385e-01 ,  1.49876401e-01 ,   1.05319373e-01 ,  5.84734641e-02 ,  1.12918485e-03 , -6.26239851e-02 ,  -1.17618337e-01 , -1.69042021e-01 , -2.26355791e-01 , -2.91909546e-01 ,  -3.38908046e-01 , -3.66832495e-01 , -4.06842262e-01 , -4.52558964e-01 ,  -4.81582075e-01 , -4.88631845e-01 , -4.96230960e-01 , -5.09628594e-01 ,  -5.05294979e-01 , -4.87197489e-01 , -4.73342091e-01 , -4.64552760e-01 ,  -4.47706521e-01 , -4.21308011e-01 , -3.88927877e-01 , -3.51634264e-01 ,  -3.33170563e-01 , -3.32285523e-01 , -3.21909249e-01 , -2.87087619e-01 ,  -2.54158139e-01 , -2.63466299e-01 , -2.85012364e-01 , -2.82326728e-01 ,  -2.67921984e-01 , -2.76894450e-01 , -3.06924641e-01 , -3.28409672e-01 ,  -3.38755459e-01 , -3.54167312e-01 , -3.70311588e-01 , -3.78093809e-01 ,  -3.87463003e-01 , -4.03302103e-01 , -4.17126983e-01 , -4.16058838e-01 ,  -4.08581793e-01 , -3.96984786e-01 , -3.78856778e-01 , -3.63841683e-01 ,  -3.53679001e-01 , -3.37199003e-01 , -2.98806727e-01 , -2.57301539e-01 ,  -2.32428968e-01 , -2.13660091e-01 , -1.83324680e-01 , -1.44322038e-01 ,  -1.15024261e-01 , -9.06094536e-02 , -6.11285754e-02 , -3.21054719e-02 ,  -1.10171819e-02 ,  6.40888698e-03 ,  2.96945106e-02 ,  5.57878353e-02 ,   7.34275356e-02 ,  8.72524157e-02 ,  1.02694787e-01 ,  1.16977446e-01 ,   1.29184857e-01 ,  1.41819507e-01 ,  1.56376839e-01 ,  1.64647356e-01 ,   1.69804990e-01 ,  1.84972689e-01 ,  2.02520832e-01 ,  2.09418014e-01 ,   2.06915498e-01 ,  2.10180968e-01 ,  2.21381262e-01 ,  2.28980377e-01 ,   2.35999629e-01 ,  2.41798148e-01 ,  2.39905998e-01 ,  2.27332383e-01 ,   2.20740378e-01 ,  2.30964079e-01 ,  2.40760520e-01 ,  2.41737112e-01 ,   2.33588666e-01 ,  2.28400528e-01 ,  2.26355791e-01 ,  2.27454454e-01 ,   2.36701563e-01 ,  2.45735034e-01 ,  2.47322008e-01 ,  2.42439047e-01 ,   2.42530599e-01 ,  2.51899779e-01 ,  2.64198750e-01 ,  2.69447923e-01 ,   2.63893545e-01 ,  2.60017693e-01 ,  2.62733847e-01 ,  2.68196672e-01 ,   2.71340072e-01 ,  2.72957563e-01 ,  2.71309555e-01 ,  2.64320821e-01 ,   2.59224206e-01 ,  2.62672812e-01 ,  2.65755177e-01 ,  2.58796960e-01 ,   2.49366745e-01 ,  2.48634294e-01 ,  2.57606745e-01 ,  2.61177391e-01 ,   2.62581259e-01 ,  2.63710439e-01 ,  2.63344228e-01 ,  2.64595479e-01 ,   2.72713393e-01 ,  2.92458862e-01 ,  3.08145404e-01 ,  3.12906265e-01 ,   3.14859450e-01 ,  3.22275460e-01 ,  3.34147155e-01 ,  3.43668938e-01 ,   3.50108355e-01 ,  3.49040180e-01 ,  3.40159297e-01 ,  3.24991614e-01 ,   3.14340651e-01 ,  3.06711018e-01 ,  2.85439610e-01 ,  2.51014739e-01 ,   2.05908388e-01 ,  1.58848837e-01 ,  1.15512557e-01 ,  7.32749403e-02 ,   3.02133244e-02 , -2.47810297e-02 , -8.86867866e-02 , -1.51432842e-01 ,  -2.11706907e-01 , -2.64198750e-01 , -3.10037524e-01 , -3.46018851e-01 ,  -3.78185362e-01 , -4.20972317e-01 , -4.64369655e-01 , -4.92294073e-01 ,  -4.97421175e-01 , -4.90981787e-01 , -4.87807870e-01 , -4.86800730e-01 ,  -4.82070386e-01 , -4.68581200e-01 , -4.47798103e-01 , -4.20819730e-01 ,  -3.90606403e-01 , -3.54533523e-01 , -3.26273382e-01 , -3.20993692e-01 ,  -3.14737380e-01 , -2.90536225e-01 , -2.59773552e-01 , -2.46833712e-01 ,  -2.62459189e-01 , -2.69264817e-01 , -2.63466299e-01 , -2.65663624e-01 ,  -2.82540351e-01 , -3.06649983e-01 , -3.21634561e-01 , -3.36588651e-01 ,  -3.53953660e-01 , -3.66222113e-01 , -3.77849668e-01 , -3.91125232e-01 ,  -4.00830090e-01 , -3.97686690e-01 , -3.91277820e-01 , -3.90118092e-01 ,  -3.82335901e-01 , -3.64665657e-01 , -3.43363762e-01 , -3.24533820e-01 ,  -2.98257381e-01 , -2.61879325e-01 , -2.31910154e-01 , -2.09112823e-01 ,  -1.82622761e-01 , -1.43436998e-01 , -1.01260416e-01 , -7.26645738e-02 ,  -5.07522821e-02 , -2.82601397e-02 , -5.49333170e-03 ,  1.83721427e-02 ,   4.10168767e-02 ,  6.38752431e-02 ,  8.04162696e-02 ,  8.82595330e-02 ,   9.64384899e-02 ,  1.06814787e-01 ,  1.20365001e-01 ,  1.37607962e-01 ,   1.51493877e-01 ,  1.60954624e-01 ,  1.62419513e-01 ,  1.68736845e-01 ,   1.83629870e-01 ,  1.92663357e-01 ,  1.98065132e-01 ,  2.00720236e-01 ,   2.07708970e-01 ,  2.14453563e-01 ,  2.17780083e-01 ,  2.20557272e-01 ,   2.19824821e-01 ,  2.21137121e-01 ,  2.19794303e-01 ,  2.14026302e-01 ,   2.11767942e-01 ,  2.13019192e-01 ,  2.16742456e-01 ,  2.15033412e-01 ,   2.09051788e-01 ,  2.07373276e-01 ,  2.09875792e-01 ,  2.16040522e-01 ,   2.23853260e-01 ,  2.27240816e-01 ,  2.27118745e-01 ,  2.29010895e-01 ,   2.35816523e-01 ,  2.45429859e-01 ,  2.51808226e-01 ,  2.53120512e-01 ,   2.53212065e-01 ,  2.54310727e-01 ,  2.54463345e-01 ,  2.51991332e-01 ,   2.49732956e-01 ,  2.49794006e-01 ,  2.47932374e-01 ,  2.39753410e-01 ,   2.26081118e-01 ,  2.10638747e-01 ,  2.03833118e-01 ,  2.08227783e-01 ,   2.15216532e-01 ,  2.20831931e-01 ,  2.14178905e-01 ,  2.03588977e-01 ,   2.03497425e-01 ,  2.24585712e-01 ,  2.53395170e-01 ,  2.75673687e-01 ,   2.93252349e-01 ,  3.04177970e-01 ,  3.14340651e-01 ,  3.26548040e-01 ,   3.56913954e-01 ,  3.93780321e-01 ,  4.13190097e-01 ,  4.14075136e-01 ,   4.01959300e-01 ,  3.93108934e-01 ,  3.89996022e-01 ,  3.88317525e-01 ,   3.82335901e-01 ,  3.49192798e-01 ,  3.00180048e-01 ,  2.45094150e-01 ,   1.93853572e-01 ,  1.50334179e-01 ,  9.79033783e-02 ,  4.16272469e-02 ,  -2.45368816e-02 , -9.49736014e-02 , -1.61809132e-01 , -2.29834899e-01 ,  -2.92458862e-01 , -3.41013819e-01 , -3.76567900e-01 , -4.12915438e-01 ,  -4.57899719e-01 , -5.00808716e-01 , -5.27573466e-01 , -5.31937599e-01 ,  -5.21439254e-01 , -5.05600154e-01 , -4.89577919e-01 , -4.83230084e-01 ,  -4.77584153e-01 , -4.57350373e-01 , -4.21735287e-01 , -3.76506865e-01 ,  -3.31858277e-01 , -2.96792507e-01 , -2.91055024e-01 , -2.99722284e-01 ,  -2.81472206e-01 , -2.43812367e-01 , -2.20313117e-01 , -2.34229565e-01 ,  -2.56599635e-01 , -2.62062430e-01 , -2.73049116e-01 , -2.97189236e-01 ,  -3.22977394e-01 , -3.43058556e-01 , -3.66710424e-01 , -3.95886093e-01 ,  -4.10870701e-01 , -4.21613216e-01 , -4.38642532e-01 , -4.52864170e-01 ,  -4.54115421e-01 , -4.49232459e-01 , -4.48866248e-01 , -4.35651720e-01 ,  -4.00128186e-01 , -3.68816197e-01 , -3.54838699e-01 , -3.35428923e-01 ,  -2.91879028e-01 , -2.39936516e-01 , -2.03314304e-01 , -1.74199656e-01 ,  -1.41758472e-01 , -9.99175981e-02 , -5.98467961e-02 , -2.83822138e-02 ,  -1.22074038e-04 ,  2.01116987e-02 ,  4.06811722e-02 ,  6.27460554e-02 ,   8.37733075e-02 ,  1.01931825e-01 ,  1.14719078e-01 ,  1.22898035e-01 ,   1.25949889e-01 ,  1.28086179e-01 ,  1.36631370e-01 ,  1.51097134e-01 ,   1.60557881e-01 ,  1.60649434e-01 ,  1.58330023e-01 ,  1.65135652e-01 ,   1.74443796e-01 ,  1.83263645e-01 ,  1.87597275e-01 ,  1.88787505e-01 ,   1.91228986e-01 ,  1.95745721e-01 ,  2.05725268e-01 ,  2.12530896e-01 ,   2.17566460e-01 ,  2.13812679e-01 ,  2.05114901e-01 ,  2.07434312e-01 ,   2.20496237e-01 ,  2.30048522e-01 ,  2.27912232e-01 ,  2.26477861e-01 ,   2.23487049e-01 ,  2.28614151e-01 ,  2.41554007e-01 ,  2.53028959e-01 ,   2.55470455e-01 ,  2.49977112e-01 ,  2.59865105e-01 ,  2.76314586e-01 ,   2.90017396e-01 ,  2.90597260e-01 ,  2.84615606e-01 ,  2.86202580e-01 ,   2.87575901e-01 ,  2.90597260e-01 ,  2.91207612e-01 ,  2.93191314e-01 ,   2.92214721e-01 ,  2.85897404e-01 ,  2.75276959e-01 ,  2.57820368e-01 ,   2.47016817e-01 ,  2.48207033e-01 ,  2.56172359e-01 ,  2.56965846e-01 ,   2.48786896e-01 ,  2.38196969e-01 ,  2.30262160e-01 ,  2.27912232e-01 ,   2.42225409e-01 ,  2.74239331e-01 ,  3.11410874e-01 ,  3.26853245e-01 ,   3.16507459e-01 ,  3.04055899e-01 ,  3.12082291e-01 ,  3.54838699e-01 ,   4.01776165e-01 ,  4.25000757e-01 ,  4.11786258e-01 ,  3.69792789e-01 ,   3.33414704e-01 ,  3.27066869e-01 ,  3.39030117e-01 ,  3.34971160e-01 ,   2.96365231e-01 ,  2.25348681e-01 ,  1.46610916e-01 ,  7.78527185e-02 ,   2.97555476e-02 , -9.36918240e-03 , -5.76189458e-02 , -1.23874627e-01 ,  -2.09051788e-01 , -2.88125247e-01 , -3.53648484e-01 , -4.00769055e-01 ,  -4.27442253e-01 , -4.44471568e-01 , -4.68855858e-01 , -5.11673331e-01 ,  -5.46159267e-01 , -5.45457304e-01 , -5.25009930e-01 , -5.07278681e-01 ,  -4.84908611e-01 , -4.53444004e-01 , -4.20392454e-01 , -3.96710098e-01 ,  -3.78368467e-01 , -3.51115465e-01 , -3.08542132e-01 , -2.56202877e-01 ,  -2.16345713e-01 , -2.13782161e-01 , -2.33558148e-01 , -2.42408514e-01 ,  -2.30628371e-01 , -2.28705704e-01 , -2.48939484e-01 , -2.71950424e-01 ,  -2.91634887e-01 , -3.21848214e-01 , -3.73790711e-01 , -4.20636624e-01 ,  -4.49201941e-01 , -4.61958677e-01 , -4.71816152e-01 , -4.91195410e-01 ,  -5.19547105e-01 , -5.42191863e-01 , -5.38743258e-01 , -5.08499384e-01 ,  -4.85213786e-01 , -4.74868000e-01 , -4.51673955e-01 , -4.07208472e-01 ,  -3.58989239e-01 , -3.25022131e-01 , -2.79549539e-01 , -2.22449422e-01 ,  -1.69377729e-01 , -1.29795223e-01 , -9.91241187e-02 , -6.17999807e-02 ,  -1.97149571e-02 ,  1.92876980e-02 ,  5.39872423e-02 ,  7.19321296e-02 ,   7.57774562e-02 ,  8.34681243e-02 ,  1.01107821e-01 ,  1.21127963e-01 ,   1.27414778e-01 ,  1.32663965e-01 ,  1.34495065e-01 ,  1.28604993e-01 ,   1.22867517e-01 ,  1.29154339e-01 ,  1.49571210e-01 ,  1.66814178e-01 ,   1.71361431e-01 ,  1.64372697e-01 ,  1.61870182e-01 ,  1.69255659e-01 ,   1.87963501e-01 ,  2.09692672e-01 ,  2.23883793e-01 ,  2.25745410e-01 ,   2.24921420e-01 ,  2.25836977e-01 ,  2.34687343e-01 ,  2.49855042e-01 ,   2.60811180e-01 ,  2.64137685e-01 ,  2.63435781e-01 ,  2.60994285e-01]   )

    # sample_rate = 16000  # 采样率
    # duration = 2.0       # 持续时间（秒）
    # frequency = 440.0    # 频率（Hz）

    # t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    # audio_array = np.sin(2 * np.pi * frequency * t).astype(np.float32)  # 形状为 [采样点数]
    # print(data.shape)
    # print(audio_array.shape)
    # res = model.generate(
    #         input=audio_array,
    #         cache={},
    #         language="auto",  # "zn", "en", "yue", "ja", "ko", "nospeech"
    #         use_itn=True,
    #         batch_size_s=60,
    #         merge_vad=True,  #
    #         merge_length_s=15,
    #     )
    # text = rich_transcription_postprocess(res[0]["text"])
    # print(text)
