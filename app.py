# libraly
import streamlit as st

# write 
st.title('Software Perkalian')
st.subheader('Ini adalah aplikasi untuk mengalikan bilangan bulat')

#input bilangan pertama 
number1 = st.number_input('Masukkin lah angkanya')
st.write(f'Bilangan pertamanya ni {number1}')

#Input bilangan kedua
number2 = st.number_input('Masukkin lah angka keduanya')
st.write(f'Bilangan keduanya ni {number2}')

#Hasil kali
hasil = number1*number2

if st.button('Hitung'):
    st.write(f'Hasil kali antara {number1} dan {number2} adalah {hasil}')
else:
    st.write('Silakan pencet tombol hitung')

