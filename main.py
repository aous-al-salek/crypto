from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from aes import aes_encrypt, aes_decrypt
from des import des_encrypt, des_decrypt
from des3 import des3_encrypt, des3_decrypt
from ascon_cipher import ascon128_encrypt, ascon128_decrypt, ascon128a_encrypt, ascon128a_decrypt, ascon80pq_encrypt, ascon80pq_decrypt
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
    ascon128_encrypt_time = []
    ascon128_decrypt_time = []
    ascon128a_encrypt_time = []
    ascon128a_decrypt_time = []
    ascon80pq_encrypt_time = []
    ascon80pq_decrypt_time = []

    msg = b"Cryptology is awesome!"
    #msg = b"0".zfill(1000000)

    for i in range(10):
        key56 = get_random_bytes(8)
        key128 = get_random_bytes(16)
        key160 =  get_random_bytes(20)
        key192 = get_random_bytes(24)
        key256 =  get_random_bytes(32)
        
        while True:
            try:
                key168 = DES3.adjust_key_parity(get_random_bytes(24))
                break
            except ValueError:
                pass
        
        for i in range(1):
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

            st = perf_counter_ns()
            ascon_en_128 = ascon128_encrypt(msg, key128)
            et = perf_counter_ns()
            ascon128_encrypt_time.append(et-st)
            
            st = perf_counter_ns()
            ascon_dec_128 = ascon128_decrypt(ascon_en_128, key128)
            et = perf_counter_ns()
            ascon128_decrypt_time.append(et-st)
    
            st = perf_counter_ns()
            ascon_en_128a = ascon128a_encrypt(msg, key128)
            et = perf_counter_ns()
            ascon128a_encrypt_time.append(et-st)
    
            st = perf_counter_ns()
            ascon_dec_128a = ascon128a_decrypt(ascon_en_128a, key128)
            et = perf_counter_ns()
            ascon128a_decrypt_time.append(et-st)
    
            st = perf_counter_ns()
            ascon_en_80pq = ascon80pq_encrypt(msg, key160)
            et = perf_counter_ns()
            ascon80pq_encrypt_time.append(et-st)
    
            st = perf_counter_ns()
            ascon_dec_80pq = ascon80pq_decrypt(ascon_en_80pq, key160)
            et = perf_counter_ns()
            ascon80pq_decrypt_time.append(et-st)


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
    mean_ascon128_encrypt_time = mean(ascon128_encrypt_time)
    mean_ascon128_decrypt_time = mean(ascon128_decrypt_time)
    mean_ascon128a_encrypt_time = mean(ascon128a_encrypt_time)
    mean_ascon128a_decrypt_time = mean(ascon128a_decrypt_time)
    mean_ascon80pq_encrypt_time = mean(ascon80pq_encrypt_time)
    mean_ascon80pq_decrypt_time = mean(ascon80pq_decrypt_time)

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
        results_file.write("TDES,168 bits,Decryption,{m}\n".format(m=round(mean_des3_dec_168_time/1000, 3)))
        results_file.write("Ascon-128,128 bits,Encryption,{m}\n".format(m=round(mean_ascon128_encrypt_time/1000, 3)))
        results_file.write("Ascon-128,128 bits,Decryption,{m}\n".format(m=round(mean_ascon128_decrypt_time/1000, 3)))
        results_file.write("Ascon-128a,128 bits,Encryption,{m}\n".format(m=round(mean_ascon128a_encrypt_time/1000, 3)))
        results_file.write("Ascon-128a,128 bits,Decryption,{m}\n".format(m=round(mean_ascon128a_decrypt_time/1000, 3)))
        results_file.write("Ascon-80pq,160 bits,Encryption,{m}\n".format(m=round(mean_ascon80pq_encrypt_time/1000, 3)))
        results_file.write("Ascon-80pq,160 bits,Decryption,{m}".format(m=round(mean_ascon80pq_decrypt_time/1000, 3)))
        results_file.close()

if __name__ == "__main__":
    main()
