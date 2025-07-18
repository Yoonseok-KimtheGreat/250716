import streamlit as st
import time

# 페이지 설정
st.set_page_config(
    page_title="MBTI 여행지 추천 ✈️",
    page_icon="🌍",
    layout="wide"
)

# MBTI별 여행지 데이터
MBTI_DESTINATIONS = {
    "INTJ": {
        "destinations": ["일본 교토", "그리스 산토리니", "아이슬란드 레이캬비크"],
        "spots": {
            "일본 교토": "🏯 킨카쿠지(금각사) - 완벽한 건축미와 조용한 사색 공간으로 INTJ의 내향적 성찰을 도와줍니다",
            "그리스 산토리니": "🌅 이아 마을 - 체계적으로 설계된 아름다운 건축물들이 INTJ의 완벽주의 성향을 만족시킵니다",
            "아이슬란드 레이캬비크": "❄️ 블루라군 - 신비로운 자연 현상과 과학적 원리가 INTJ의 지적 호기심을 자극합니다"
        }
    },
    "INTP": {
        "destinations": ["독일 베를린", "체코 프라하", "네덜란드 암스테르담"],
        "spots": {
            "독일 베를린": "🏛️ 베를린 박물관 섬 - 다양한 분야의 지식과 역사적 통찰을 제공하여 INTP의 탐구욕을 충족시킵니다",
            "체코 프라하": "🌉 카를교 - 중세 건축의 논리적 구조와 예술적 아름다움이 INTP의 분석적 사고를 자극합니다",
            "네덜란드 암스테르담": "🚲 운하 투어 - 체계적인 도시 설계와 독특한 문화가 INTP의 창의적 사고를 활성화합니다"
        }
    },
    "ENTJ": {
        "destinations": ["미국 뉴욕", "싱가포르", "영국 런던"],
        "spots": {
            "미국 뉴욕": "🏙️ 타임스퀘어 - 역동적인 비즈니스 환경과 리더십의 상징적 공간으로 ENTJ의 야망을 자극합니다",
            "싱가포르": "🌆 마리나 베이 샌즈 - 혁신적인 건축과 효율적인 도시 계획이 ENTJ의 전략적 사고를 만족시킵니다",
            "영국 런던": "👑 빅벤 - 전통과 현대가 조화된 글로벌 리더십의 중심지로 ENTJ의 비전을 확장시킵니다"
        }
    },
    "ENTP": {
        "destinations": ["태국 방콕", "스페인 바르셀로나", "브라질 리우데자네이루"],
        "spots": {
            "태국 방콕": "🛺 카오산로드 - 다양한 문화와 사람들이 만나는 활기찬 공간으로 ENTP의 호기심을 자극합니다",
            "스페인 바르셀로나": "🏛️ 사그라다 파밀리아 - 독창적이고 혁신적인 건축물이 ENTP의 창의성을 영감으로 채워줍니다",
            "브라질 리우데자네이루": "🎭 카니발 - 자유롭고 역동적인 축제 문화가 ENTP의 모험 정신을 만족시킵니다"
        }
    },
    "INFJ": {
        "destinations": ["인도 리시케시", "페루 마추픽추", "부탄 팀푸"],
        "spots": {
            "인도 리시케시": "🧘 요가 센터 - 영적 성장과 내면 탐구의 성지로 INFJ의 깊은 사색을 도와줍니다",
            "페루 마추픽추": "🏔️ 잉카 유적 - 신비로운 고대 문명의 흔적이 INFJ의 직관적 통찰력을 자극합니다",
            "부탄 팀푸": "🙏 타이거 네스트 - 평화롭고 영적인 환경이 INFJ의 내향적 성격과 완벽하게 조화됩니다"
        }
    },
    "INFP": {
        "destinations": ["프랑스 프로방스", "캐나다 밴쿠버", "뉴질랜드 퀸스타운"],
        "spots": {
            "프랑스 프로방스": "🌻 라벤더 밭 - 로맨틱하고 예술적인 풍경이 INFP의 감성적 영감을 자극합니다",
            "캐나다 밴쿠버": "🌲 스탠리 파크 - 자연과 도시가 조화된 평화로운 공간으로 INFP의 이상주의를 실현합니다",
            "뉴질랜드 퀸스타운": "🏔️ 밀포드 사운드 - 순수하고 아름다운 자연이 INFP의 순수한 마음을 치유해줍니다"
        }
    },
    "ENFJ": {
        "destinations": ["이탈리아 로마", "멕시코 칸쿤", "인도네시아 발리"],
        "spots": {
            "이탈리아 로마": "⛪ 콜로세움 - 역사적 웅장함과 인간 드라마가 ENFJ의 감정적 공감력을 자극합니다",
            "멕시코 칸쿤": "🏖️ 치첸이트사 - 다양한 문화 체험과 사람들과의 만남이 ENFJ의 사교성을 만족시킵니다",
            "인도네시아 발리": "🌺 우붓 - 따뜻한 현지인들과의 교류가 ENFJ의 타인에 대한 관심을 충족시킵니다"
        }
    },
    "ENFP": {
        "destinations": ["호주 시드니", "모로코 마라케시", "콜롬비아 카르타헤나"],
        "spots": {
            "호주 시드니": "🏄 본다이 비치 - 활기찬 해변 문화와 다양한 액티비티가 ENFP의 에너지를 충전시킵니다",
            "모로코 마라케시": "🕌 제마 엘 프나 광장 - 이국적이고 다채로운 문화 체험이 ENFP의 모험심을 자극합니다",
            "콜롬비아 카르타헤나": "💃 구시가지 - 열정적인 라틴 문화와 따뜻한 사람들이 ENFP의 외향성을 만족시킵니다"
        }
    },
    "ISTJ": {
        "destinations": ["독일 뮌헨", "일본 나라", "스위스 베른"],
        "spots": {
            "독일 뮌헨": "🍺 마리엔플라츠 - 전통과 질서가 잘 보존된 광장이 ISTJ의 안정감을 제공합니다",
            "일본 나라": "🦌 도다이지 - 오랜 역사와 전통이 체계적으로 보존된 곳으로 ISTJ의 보수적 성향에 맞습니다",
            "스위스 베른": "⏰ 지트글로케 - 정확성과 질서를 중시하는 문화가 ISTJ의 가치관과 일치합니다"
        }
    },
    "ISFJ": {
        "destinations": ["오스트리아 잘츠부르크", "덴마크 코펜하겐", "캐나다 토론토"],
        "spots": {
            "오스트리아 잘츠부르크": "🎼 모차르트 생가 - 평화롭고 아름다운 음악의 도시가 ISFJ의 온화한 성격을 위로합니다",
            "덴마크 코펜하겐": "🧜‍♀️ 인어공주 동상 - 동화 같은 따뜻한 분위기가 ISFJ의 보호본능을 만족시킵니다",
            "캐나다 토론토": "🍁 CN타워 - 안전하고 다문화적인 환경이 ISFJ의 배려심 깊은 성격에 적합합니다"
        }
    },
    "ESTJ": {
        "destinations": ["중국 베이징", "러시아 모스크바", "아랍에미리트 두바이"],
        "spots": {
            "중국 베이징": "🏯 자금성 - 체계적이고 위계질서가 분명한 건축물이 ESTJ의 조직력을 자극합니다",
            "러시아 모스크바": "🏛️ 크렘린 궁전 - 권위와 전통이 잘 보존된 곳으로 ESTJ의 리더십을 인정받습니다",
            "아랍에미리트 두바이": "🏗️ 부르즈 할리파 - 효율적이고 체계적인 도시 개발이 ESTJ의 실용주의를 만족시킵니다"
        }
    },
    "ESFJ": {
        "destinations": ["터키 이스탄불", "그리스 아테네", "포르투갈 리스본"],
        "spots": {
            "터키 이스탄불": "🕌 블루 모스크 - 따뜻한 환대 문화와 아름다운 건축이 ESFJ의 사교성을 충족시킵니다",
            "그리스 아테네": "🏛️ 파르테논 신전 - 고전적 아름다움과 조화로운 문화가 ESFJ의 전통적 가치관에 맞습니다",
            "포르투갈 리스본": "🚋 알파마 지구 - 친근하고 따뜻한 동네 분위기가 ESFJ의 공동체 의식을 만족시킵니다"
        }
    },
    "ISTP": {
        "destinations": ["노르웨이 베르겐", "칠레 파타고니아", "몽골 울란바토르"],
        "spots": {
            "노르웨이 베르겐": "🏔️ 플뢰이엔 산 - 실용적인 등산과 장인 정신이 깃든 목조 건축이 ISTP의 기술적 관심을 자극합니다",
            "칠레 파타고니아": "🏕️ 토레스 델 파이네 - 야생적이고 도전적인 자연환경이 ISTP의 모험 정신을 만족시킵니다",
            "몽골 울란바토르": "🐎 초원 승마 - 자유롭고 독립적인 유목 문화가 ISTP의 개인주의적 성향에 맞습니다"
        }
    },
    "ISFP": {
        "destinations": ["일본 후지산", "크로아티아 두브로브니크", "필리핀 보라카이"],
        "spots": {
            "일본 후지산": "🌸 하코네 - 자연의 아름다움과 예술적 감성이 ISFP의 미적 감각을 자극합니다",
            "크로아티아 두브로브니크": "🏰 구시가지 - 조용하고 아름다운 중세 도시가 ISFP의 평화로운 성격에 맞습니다",
            "필리핀 보라카이": "🏖️ 화이트 비치 - 순수하고 자연스러운 해변이 ISFP의 자유로운 영혼을 치유합니다"
        }
    },
    "ESTP": {
        "destinations": ["베트남 호치민", "아르헨티나 부에노스아이레스", "남아공 케이프타운"],
        "spots": {
            "베트남 호치민": "🏍️ 벤탄 시장 - 활기찬 거리와 즉흥적인 모험이 ESTP의 현재 지향적 성격을 자극합니다",
            "아르헨티나 부에노스아이레스": "💃 탱고 클럽 - 열정적이고 즉흥적인 춤 문화가 ESTP의 활동적 성향을 만족시킵니다",
            "남아공 케이프타운": "🦁 사파리 - 스릴 넘치는 야생 동물 관찰이 ESTP의 모험심을 충족시킵니다"
        }
    },
    "ESFP": {
        "destinations": ["이집트 카이로", "쿠바 아바나", "인도 고아"],
        "spots": {
            "이집트 카이로": "🐪 기자 피라미드 - 웅장하고 신비로운 고대 문명이 ESFP의 호기심을 자극합니다",
            "쿠바 아바나": "🎺 말레콘 거리 - 자유분방하고 음악이 넘치는 문화가 ESFP의 표현력을 만족시킵니다",
            "인도 고아": "🌴 안주나 비치 - 다채로운 축제와 자유로운 분위기가 ESFP의 사교적 성격에 맞습니다"
        }
    }
}

# 메인 UI
def main():
    # 헤더
    st.title("🌍 MBTI 기반 여행지 추천")
    st.subheader("당신의 성격에 맞는 완벽한 여행지를 찾아보세요! ✈️")
    
    # MBTI 선택
    st.markdown("### 🧠 당신의 MBTI 유형을 선택해주세요")
    
    # 4개 그룹으로 나누어 선택하기 쉽게 구성
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("**📊 분석가 (NT)**")
        nt_types = ["INTJ", "INTP", "ENTJ", "ENTP"]
        
    with col2:
        st.markdown("**🌟 외교관 (NF)**")
        nf_types = ["INFJ", "INFP", "ENFJ", "ENFP"]
        
    with col3:
        st.markdown("**🛡️ 관리자 (SJ)**")
        sj_types = ["ISTJ", "ISFJ", "ESTJ", "ESFJ"]
        
    with col4:
        st.markdown("**🎭 탐험가 (SP)**")
        sp_types = ["ISTP", "ISFP", "ESTP", "ESFP"]
    
    # 전체 MBTI 목록
    all_types = nt_types + nf_types + sj_types + sp_types
    
    selected_mbti = st.selectbox(
        "MBTI 유형 선택",
        options=all_types,
        format_func=lambda x: f"{x} - {get_mbti_description(x)}"
    )
    
    # 추천 버튼
    if st.button("🎯 나만의 여행지 추천받기!", type="primary"):
        # 풍선 효과
        st.balloons()
        
        # 로딩 효과
        with st.spinner('✨ 당신만을 위한 여행지를 찾고 있습니다...'):
            time.sleep(1)
        
        # 추천 결과 표시
        show_recommendations(selected_mbti)

def get_mbti_description(mbti_type):
    descriptions = {
        "INTJ": "건축가", "INTP": "논리술사", "ENTJ": "통솔자", "ENTP": "변론가",
        "INFJ": "옹호자", "INFP": "중재자", "ENFJ": "선도자", "ENFP": "활동가",
        "ISTJ": "물류담당자", "ISFJ": "수호자", "ESTJ": "경영자", "ESFJ": "집정관",
        "ISTP": "만능재주꾼", "ISFP": "모험가", "ESTP": "사업가", "ESFP": "연예인"
    }
    return descriptions.get(mbti_type, "")

def show_recommendations(mbti_type):
    st.markdown("---")
    st.markdown(f"## 🎉 {mbti_type} 유형을 위한 특별 추천지")
    
    # 성공 메시지
    st.success(f"🎯 {mbti_type} 유형에게 완벽한 여행지를 찾았습니다!")
    
    destinations = MBTI_DESTINATIONS[mbti_type]["destinations"]
    spots = MBTI_DESTINATIONS[mbti_type]["spots"]
    
    # 3개 여행지를 컬럼으로 표시
    col1, col2, col3 = st.columns(3)
    
    for i, (destination, col) in enumerate(zip(destinations, [col1, col2, col3])):
        with col:
            st.markdown(f"### 🌟 {destination}")
            
            # 각 여행지의 추천 관광지
            spot_info = spots[destination]
            
            # 정보 박스
            st.info(f"**추천 관광지:**\n{spot_info}")
            
            # 여행 팁
            st.markdown("---")
            st.markdown(f"**💡 {mbti_type} 타입을 위한 팁:**")
            tip = get_travel_tip(mbti_type, destination)
            st.markdown(tip)
    
    # 추가 정보
    st.markdown("---")
    st.markdown("### 🎒 여행 준비 완료!")
    st.markdown(f"**{mbti_type}** 유형의 당신에게 이 여행지들이 특별한 경험을 선사할 것입니다!")
    
    # 다시 추천받기 버튼
    if st.button("🔄 다른 MBTI로 다시 추천받기"):
        st.rerun()

def get_travel_tip(mbti_type, destination):
    tips = {
        "INTJ": "📚 사전에 충분한 정보를 수집하고 체계적인 일정을 세워보세요",
        "INTP": "🔍 현지의 독특한 문화와 역사적 배경을 깊이 탐구해보세요",
        "ENTJ": "🎯 명확한 목표를 설정하고 효율적인 동선을 계획하세요",
        "ENTP": "🎭 즉흥적인 모험과 현지인들과의 교류를 즐겨보세요",
        "INFJ": "🧘 혼자만의 사색 시간을 충분히 갖고 의미 있는 경험을 추구하세요",
        "INFP": "🎨 감성적인 순간들을 기록하고 자신만의 속도로 여행하세요",
        "ENFJ": "👥 현지인들과의 만남을 통해 따뜻한 인간관계를 만들어보세요",
        "ENFP": "🌈 새로운 경험에 열린 마음으로 다양한 활동을 시도해보세요",
        "ISTJ": "📋 안전하고 검증된 여행 코스를 선택하고 충분한 준비를 하세요",
        "ISFJ": "💝 동반자와 함께하는 평화로운 여행을 계획해보세요",
        "ESTJ": "⏰ 시간 관리를 철저히 하고 주요 명소를 놓치지 않도록 하세요",
        "ESFJ": "🤝 그룹 투어나 현지 가이드와 함께하는 여행을 추천합니다",
        "ISTP": "🛠️ 실용적인 장비를 준비하고 자유로운 일정을 짜보세요",
        "ISFP": "🌸 아름다운 자연과 예술적 공간에서 충분한 휴식을 취하세요",
        "ESTP": "⚡ 스릴 넘치는 액티비티와 현지 음식을 적극적으로 체험하세요",
        "ESFP": "🎉 축제나 이벤트가 있는 시기를 노려 활기찬 여행을 즐기세요"
    }
    return tips.get(mbti_type, "즐거운 여행 되세요! 🌟")

if __name__ == "__main__":
    main()
