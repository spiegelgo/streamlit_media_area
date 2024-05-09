# streamlit_media_area
 
해당 데이터는 문화 빅데이터 플랫폼에서 내려받았으며<br/>
한국 문화 정보원에서 제공한<br/>
KC_MEDIA_VIDO_AREA_DATA_2023.csv를 사용하였음<br/>
https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=462fe230-0334-11ee-a67e-69239d37dfae<br/><br/>

데이터를 보자마자 아, 이런걸 만들면 좋겠다 싶어 바로 제작하게 되었고<br/>
평소에 어딘가에 놀러갔을때,<br/>
어디로 놀러가고 싶을때,<br/>
티비에 나왔던 그 곳, 영화에 나왔던 그 곳을<br/>
한 번쯤 가보고싶다 하고 생각이 들 때가 있었던적이 있을것이다<br/><br/>

그래서 이 데이터를 보자마자 그런 생각이 들었다<br/>
주소(시군구 정도)를 검색했을 때,<br/>
미디어타입(영화,드라마 etc..)을 검색했을 때,<br/>
드라마제목, 영화제목을 검색했을 때,<br/>
장소(카페, 식당, 공원etc..)에 대해 검색했을 때<br/><br/>

그 장소를 찾을 수 있다면,<br/>
그 장소를 지도로 확인 할 수 있다면<br/>
좋겠다고<br/><br/>

그런데 마침 그 장소의 이름, 그 장소의 역할(카페,식당 등), 주소 정보,<br/>
미디어속에서 그 장소가 어떤 장면으로 나왔었는지의 정보 또한<br/>
있었기에 활용도 가능했고 또 그런 점이 좋게 생각됐다<br/><br/>

그래서 작업 과정은 일단 필요없는 데이터는 삭제처리 하였고<br/>
컬럼이 전부 영어로 되어있었기에 한글로 변경<br/>
미디어유형,장소유형 또한 영어로 되어있었기에 한글로 변경하였고,<br/><br/>

휴식시간같은경우 정보없음이라는 데이터가 발견되어<br/>
삭제 해야하나 생각했지만, 정보없음이 차지하는 데이터가 8,90퍼센트 정도였고<br/>
다시 생각해보니 그 정보가 없다는게 무조건 지워야하는게 아니라고 생각하게 된것이<br/>
비워져있는 그 정보가 다른 정보에 비해 큰 정보가 되지 못하며 있으면 좋은 정보인것이지<br/>
없다고 못 써먹을 정보가 아니었기 때문<br/><br/>


주소의 경우 서울과 서울특별시, 부산과 부산광역시, 경기도와 경기 등<br/>
이중으로 등록되어있는 경우가 있어 모두 통일 시키고 변환함<br/>

그리고 VS코드를 실행시키고 해야할 것들을 적어봤다<br/><br/>
    
1. 전체 데이터프레임<br/>
2. 첫번째는 멀티셀렉트로 미디어유형_카테고리,제목_카테고리,장소유형_카테고리,주소(아래참조)를 선택가능케하기<br/>
3. 2번째는 주소를 쪼개서 시도를 선택 시군구를 선택 할수 있게 하기<br/>
4. 해당하는것들의 데이터프레임과<br/>
5. 마지막으로 선택한 것들의 지도(위도 경도 컬럼 이용한 st.map이용)<br/><br/>

그래서 순서대로 하나 하나 만들어나갔다<br/>
중간정도로 다듬은 데이터프레임을 보여주고<br/><br/>

처음은 멀티셀렉트로 생각했지만<br/>
각각의 셀렉트박스로 각각의 카테고리컬 데이터를 선택하게끔 하는것이<br/>
사용자로서 편리하겠다고 판단, 각각의 셀렉트박스 생성<br/><br/>

그리고 주소를 표기할때에 특별시 광역시 경기도 강원도 등 크게 한번 나눈뒤<br/>
시군구 읍면동 같은 단위로 2번 선택하는것이 지도로도 보기편할것같았다<br/>
그래서 스플릿을 이용하여 0번과 1번을 새로운 주소컬럼으로 생성<br/>
0번을 선택하면 1번을 선택할수 있도록<br/><br/>

그 후에는 선택한 데이터프레임과<br/>
선택한 데이터프레임을 st.map을 이용해서 지도로 표현해보았다<br/><br/>

그 후에 테스트를 해보다가<br/>
어떤 장소가 북한에 있는걸로 표시되어<br/>
찾아본 결과 같은 장소인데 일곱번 다른매체로 등장하면서 위도경도가 모두 다르게 설정 되어있어<br/>
고쳐넣었고, 추후에 또 다른 위도경도가 틀리게 지정되어있는 부분은 수정하도록 하겠다.<br/><br/>