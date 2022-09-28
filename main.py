from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from aes import aes_encrypt, aes_decrypt
from des import des_encrypt, des_decrypt
from des3 import des3_encrypt, des3_decrypt
from time import perf_counter_ns
from statistics import mean

def main():
    aes_enc_128_time = []
    aes_dec_128_time = []
    aes_enc_192_time = []
    aes_dec_192_time = []
    aes_enc_256_time = []
    aes_dec_256_time = []
    des_enc_56_time = []
    des_dec_56_time = []
    des3_enc_168_time = []
    des3_dec_168_time = []

    #msg = b"Cryptology is awesome!"
    msg = b"0".zfill(1000000)

    for i in range(1000):
        key56 = get_random_bytes(8)
        key128 = get_random_bytes(16)
        key192 = get_random_bytes(24)
        key256 =  get_random_bytes(32)
        
        while True:
            try:
                key168 = DES3.adjust_key_parity(get_random_bytes(24))
                break
            except ValueError:
                pass
        
        for i in range(1000):
            st = perf_counter_ns()
            aes_enc_128 = aes_encrypt(msg, key128)
            et = perf_counter_ns()
            aes_enc_128_time.append(et-st)
            
            st = perf_counter_ns()
            aes_dec_128 = aes_decrypt(aes_enc_128, key128)
            et = perf_counter_ns()
            aes_dec_128_time.append(et-st)
            
            st = perf_counter_ns()
            aes_enc_192 = aes_encrypt(msg, key192)
            et = perf_counter_ns()
            aes_enc_192_time.append(et-st)
            
            st = perf_counter_ns()
            aes_dec_192 = aes_decrypt(aes_enc_192, key192)
            et = perf_counter_ns()
            aes_dec_192_time.append(et-st)
            
            st = perf_counter_ns()
            aes_enc_256 = aes_encrypt(msg, key256)
            et = perf_counter_ns()
            aes_enc_256_time.append(et-st)
            
            st = perf_counter_ns()
            aes_dec_256 = aes_decrypt(aes_enc_256, key256)
            et = perf_counter_ns()
            aes_dec_256_time.append(et-st)
            
            st = perf_counter_ns()
            des_enc_56 = des_encrypt(msg, key56)
            et = perf_counter_ns()
            des_enc_56_time.append(et-st)
            
            st = perf_counter_ns()
            des_dec_56 = des_decrypt(des_enc_56, key56)
            et = perf_counter_ns()
            des_dec_56_time.append(et-st)
            
            st = perf_counter_ns()
            des3_enc_168 = des3_encrypt(msg, key168)
            et = perf_counter_ns()
            des3_enc_168_time.append(et-st)
            
            st = perf_counter_ns()
            des3_dec_168 = des3_decrypt(des3_enc_168, key168)
            et = perf_counter_ns()
            des3_dec_168_time.append(et-st)


    mean_aes_enc_128_time = mean(aes_enc_128_time)
    mean_aes_dec_128_time = mean(aes_dec_128_time)
    mean_aes_enc_192_time = mean(aes_enc_192_time)
    mean_aes_dec_192_time = mean(aes_dec_192_time)
    mean_aes_enc_256_time = mean(aes_enc_256_time)
    mean_aes_dec_256_time = mean(aes_dec_256_time)
    mean_des_enc_56_time = mean(des_enc_56_time)
    mean_des_dec_56_time = mean(des_dec_56_time)
    mean_des3_enc_168_time = mean(des3_enc_168_time)
    mean_des3_dec_168_time = mean(des3_dec_168_time)

    with open("results.csv", "w", encoding="utf-8") as results_file:
        results_file.write("Algorithm,Key Length,Operation,Average Time in μs\n")
        results_file.write("AES,128 bits,Encryption,{m}\n".format(m=round(mean_aes_enc_128_time/1000, 3)))
        results_file.write("AES,128 bits,Decryption,{m}\n".format(m=round(mean_aes_dec_128_time/1000, 3)))
        results_file.write("AES,192 bits,Encryption,{m}\n".format(m=round(mean_aes_enc_192_time/1000, 3)))
        results_file.write("AES,192 bits,Decryption,{m}\n".format(m=round(mean_aes_dec_192_time/1000, 3)))
        results_file.write("AES,256 bits,Encryption,{m}\n".format(m=round(mean_aes_enc_256_time/1000, 3)))
        results_file.write("AES,256 bits,Decryption,{m}\n".format(m=round(mean_aes_dec_256_time/1000, 3)))
        results_file.write("DES,56 bits,Encryption,{m}\n".format(m=round(mean_des_enc_56_time/1000, 3)))
        results_file.write("DES,56 bits,Decryption,{m}\n".format(m=round(mean_des_dec_56_time/1000, 3)))
        results_file.write("TDES,168 bits,Encryption,{m}\n".format(m=round(mean_des3_enc_168_time/1000, 3)))
        results_file.write("TDES,168 bits,Decryption,{m}".format(m=round(mean_des3_dec_168_time/1000, 3)))
        results_file.close()

if __name__ == "__main__":
    main()
