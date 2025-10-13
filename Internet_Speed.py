import streamlit as st
import speedtest
st.title("Internet Speed Test")
def SpeedTest():
    if st.button("Test Speed"):
        with st.spinner("Testing your internet speed"):
    
            test=speedtest.Speedtest()
            test.get_best_server()
            
            
            download_speed=test.download()
            upload_speed=test.upload()
            ping=test.results.ping
                
                
            download_speed=round(download_speed/(10**6),2)
            upload_speed=round(upload_speed/(10**6),2)
            ping=round(ping,2)
            
            
            st.markdown(f"**Download speed:** {download_speed} Mbps")
            st.markdown(f"**Upload speed:** {upload_speed} Mbps")
            st.markdown(f"**Ping:** {ping} ms")
SpeedTest()


