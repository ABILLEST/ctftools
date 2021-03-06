from gmssl.sm4 import CryptSM4, SM4_ENCRYPT, SM4_DECRYPT

key = b'3l5butlj26hvv313'
value = b'111' #  bytes类型
iv = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' #  bytes类型
crypt_sm4 = CryptSM4()


crypt_sm4.set_key(key, SM4_ENCRYPT)
encrypt_value = crypt_sm4.crypt_ecb(value) #  bytes类型
print('加密成功！')
print('加密结果为:\n', encrypt_value)
print('\n')
crypt_sm4.set_key(key, SM4_DECRYPT)
decrypt_value = crypt_sm4.crypt_ecb(encrypt_value) #  bytes类型
print('解密成功！\n解密结果为:', decrypt_value)
print('\n')
assert value == decrypt_value
print('decrypt_value==value?',value == decrypt_value)
print('完成加解密！')