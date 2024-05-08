import streamlit as st
import pandas as pd






def run_eda() :
    st.subheader('전체의 데이터프레임을 보여드립니다')
    df = pd.read_csv('./data/media_area.csv', index_col=0)
    st.info(f'전체 데이터의 갯수는 {df.shape}입니다.')
    st.dataframe(df)
    
    '''
    여기서 보여줄 것들
    1. 전체 데이터프레임 - 완
    2. 첫번째는 멀티셀렉트로 미디어유형_카테고리,제목_카테고리,장소유형_카테고리,주소(아래참조)를 선택가능케하기 - 완
    3. 2번째는 주소를 쪼개서 시도를 선택 시군구를 선택 할수 있게 하기 - 완
    4. 해당하는것들의 데이터프레임과 - 완
    5. 마지막으로 선택한 것들의 지도(위도 경도 컬럼 이용한 st.map이용) - 완
    '''

    

    # Streamlit session state
    def session_state(**kwargs):
        for key, val in kwargs.items():
            setattr(session_state, key, val)
            
            
    # 주소 스플릿해서 첫 번째와 두 번째 값을 추출하는 함수
    def split_address(address):
        parts = address.split(' ')
        if len(parts) > 1:
            return parts[0], parts[1]
        else:
            return address, ''

    st.markdown('### 찾고 싶은 정보를 선택하여 성지를 찾아보자')
    st.markdown('#### 선택하지 않은 경우, 해당 선택지의 모든 경우를 나타냅니다.')

    st.markdown('##### 찾고자 하는 지역을 선택하세요')

    # 주소 컬럼에서 첫 번째와 두 번째 값을 추출하여 새로운 컬럼에 추가
    df[['주소_1', '주소_2']] = df['주소'].apply(split_address).tolist()

    # 주소 선택 상자 (첫 번째 카테고리)
    selected_address_1 = st.selectbox('광역자치단체', [''] + sorted(df['주소_1'].unique()))

    # 선택한 첫 번째 주소에 해당하는 두 번째 카테고리의 선택지 필터링
    if selected_address_1 != '':
        filtered_addresses_2 = df[df['주소_1'] == selected_address_1]['주소_2'].unique()
    else:
        filtered_addresses_2 = []

    # 주소 선택 상자 (두 번째 카테고리)
    selected_address_2 = st.selectbox('기초자치단체', [''] + sorted(filtered_addresses_2))

    # 선택한 주소에 따라 데이터프레임 필터링
    filtered_df = df
    if selected_address_1 != '':
        filtered_df = filtered_df[filtered_df['주소_1'] == selected_address_1]
    if selected_address_2 != '':
        filtered_df = filtered_df[filtered_df['주소_2'] == selected_address_2]

    # 미디어 유형 선택 상자
    st.markdown('##### 찾고자 하는 미디어 유형을 선택하세요')
    st.markdown('###### 영화에서 보셨던 장소인가요? 드라마? TV쇼?')
    selected_media_type = st.selectbox('해당 미디어 유형', [''] + sorted(filtered_df['미디어유형'].unique()))

    # 선택한 값에 따라 데이터프레임 필터링
    if selected_media_type != '':
        filtered_df = filtered_df[filtered_df['미디어유형'] == selected_media_type]

    st.markdown('##### 찾고자 하는 미디어 프로그램의 제목을 선택하세요')
    st.markdown('###### 위의 미디어의 유형을 먼저 선택하시면 좀 더 찾기 쉬울거에요')
    st.markdown('타이핑으로 검색도 된답니다(❁´◡`❁)')

    # 제목 선택 상자
    selected_title = st.selectbox('프로그램 제목', [''] + sorted(filtered_df['제목'].unique()))

    # 선택한 값에 따라 데이터프레임 필터링
    if selected_title != '':
        filtered_df = filtered_df[filtered_df['제목'] == selected_title]

    st.markdown('##### 찾고자 하는 장소의 유형을 선택하세요')
    st.markdown('###### 카페? 식당? 어디를 찾고 싶으세요?')

    # 장소 유형 선택 상자
    selected_location_type = st.selectbox('해당 장소 유형', [''] + sorted(filtered_df['장소유형'].unique()))

    # 선택한 값에 따라 데이터프레임 필터링
    if selected_location_type != '':
        filtered_df = filtered_df[filtered_df['장소유형'] == selected_location_type]

    # 필터링된 데이터프레임 출력
    st.dataframe(filtered_df.loc[:, '미디어유형':'주소'])
    # 위도와 경도가 있는 데이터프레임 생성
    location_df = filtered_df[['위도', '경도']]
    location_df.columns = ['LAT', 'LON']  # 컬럼 이름 변경

    # 지도에 마커 표시
    st.map(location_df)