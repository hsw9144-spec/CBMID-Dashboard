import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import platform
from io import BytesIO
from matplotlib import font_manager, rc

# ==========================================
# 1. 폰트 설정
# ==========================================
def set_font():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    font_file = os.path.join(current_dir, "NanumGothic.ttf")
    
    if os.path.exists(font_file):
        font_manager.fontManager.addfont(font_file)
        rc('font', family=font_manager.FontProperties(fname=font_file).get_name())
    else:
        try:
            if platform.system() == "Windows":
                rc('font', family="Malgun Gothic")
            elif platform.system() == "Darwin":
                rc('font', family="AppleGothic")
            else:
                rc('font', family="NanumGothic")
        except: pass
    plt.rcParams['axes.unicode_minus'] = False

st.set_page_config(page_title="CBMID Dashboard", layout="wide")
set_font()

# ==========================================
# 2. 다국어 사전
# ==========================================
TEXT = {
    "KR": {
        "title": "🌍 CBMID 글로벌 인재 지도",
        "subtitle": "AI 시대, 인류의 숨겨진 재능과 소명을 시각화하다",
        "sidebar_title": "🧬 CBMID 엔진",
        "warn_upload": "👈 왼쪽 사이드바에 CSV 파일을 업로드해주세요.",
        "tab1": "📊 전략 지도 (Strategic Matrix)",
        "tab2": "👤 개인 분석 (Individual Report)",
        "matrix_title": "CBMID 전략 매트릭스: 능력 vs 의식",
        "ideal": "이상적인 리더\n(Target Zone)",
        "danger": "위험 구간\n(High Risk)",
        "good": "선량한 시민",
        "potential": "잠재적 인재\n(Need Support)",
        "x_label": "능력 (Competence - Max Talent)",
        "y_label": "의식 (Conscience - Energy Level)",
        "select_user": "분석할 대상을 선택하세요",
        "btn_download": "💾 차트 이미지 다운로드",
        "analysis_header": "참여자 분석 결과:",
        "unit_person": "명",
        "rpt_top_int": "핵심 지능",
        "rpt_level": "의식 레벨",
        "h_superpower": "1. 당신의 핵심 무기 (Superpower)",
        "h_focus": "2. 현재 마음의 상태 (Current Focus)",
        "h_roadmap": "3. CBMID 성장 로드맵 (Growth Roadmap)",
        "radar_labels": ["언어", "논리", "공간", "신체", "음악", "대인", "성찰", "자연", "실존"],
        "mi_names": {"Linguistic": "언어 지능", "Logical": "논리-수학 지능", "Spatial": "시각-공간 지능", "Bodily": "신체-운동 지능", "Musical": "음악 지능", "Interpersonal": "대인관계 지능", "Intrapersonal": "자기성찰 지능", "Naturalist": "자연탐구 지능", "Existential": "실존 지능"},
        "int_desc": {"Linguistic": "말과 글로 사람의 마음을 움직이는 힘이 탁월합니다.", "Logical": "복잡한 현상 속에서 패턴을 찾아내는 전략적 두뇌를 가졌습니다.", "Spatial": "보이지 않는 것을 시각화하는 능력이 뛰어납니다.", "Bodily": "생각을 행동으로 구현해내는 감각이 탁월합니다.", "Musical": "소리와 리듬, 감정의 흐름을 예민하게 포착합니다.", "Interpersonal": "타인의 감정과 의도를 본능적으로 파악합니다.", "Intrapersonal": "자신을 깊이 이해하고 성찰하는 힘이 있습니다.", "Naturalist": "환경의 변화와 데이터의 패턴을 분류하는 관찰력이 뛰어납니다.", "Existential": "삶의 본질과 인류의 미래를 고민하는 철학적 사고력을 가졌습니다."},
        "lvl_desc": {1: "현재 에너지는 **'생존과 안정'**에 집중되어 있습니다.", 2: "당신은 **'책임감'**을 원동력으로 움직이고 있습니다.", 3: "당신은 **'협력과 공헌'**의 가치를 중요시합니다.", 4: "당신은 **'인류애와 포용'**의 단계에 있습니다.", 5: "당신은 **'소명과 초월'**의 에너지를 따릅니다."},
        "p_title": "💊 CBMID AI 처방전", "p_danger": "⚠️ 고위험 / 고잠재력 감지", "p_ideal": "🌟 이상적인 리더 모델", "p_grow": "💡 성장하는 인재", "p_desc_danger": "능력은 탁월하지만, 생존 본능에 갇혀 있거나 윤리가 결여되어 있습니다.", "p_desc_ideal": "능력과 양심이 조화를 이룬 이상적인 리더입니다.", "p_desc_grow": "성실하게 성장하고 있는 인재입니다."
    },
    "English": {
        "title": "🌍 CBMID Global Talent Map",
        "subtitle": "Visualizing Hidden Talents & Calling in the AI Era",
        "sidebar_title": "🧬 CBMID Engine",
        "warn_upload": "👈 Please upload CSV files in the sidebar.",
        "tab1": "📊 Strategic Matrix",
        "tab2": "👤 Individual Report",
        "matrix_title": "CBMID Strategic Map: Competence vs Conscience",
        "ideal": "Ideal Leaders\n(Target Zone)",
        "danger": "DANGER ZONE\n(High Risk)",
        "good": "Good Citizens",
        "potential": "Potential Talent\n(Need Support)",
        "x_label": "Competence (Max Talent Score)",
        "y_label": "Conscience (Energy Level)",
        "select_user": "Select User",
        "btn_download": "💾 Download Chart Image",
        "analysis_header": "Analysis of",
        "unit_person": "Participants",
        "rpt_top_int": "Top Intelligence",
        "rpt_level": "Level",
        "h_superpower": "1. Your Superpower",
        "h_focus": "2. Your Current Focus",
        "h_roadmap": "3. CBMID Growth Roadmap",
        "radar_labels": ["Ling", "Logic", "Spat", "Body", "Music", "Inter", "Intra", "Natur", "Exist"],
        "mi_names": {k: k for k in ["Linguistic", "Logical", "Spatial", "Bodily", "Musical", "Interpersonal", "Intrapersonal", "Naturalist", "Existential"]},
        "int_desc": {"Linguistic": "You have the power to move hearts with words.", "Logical": "You possess a strategic mind.", "Spatial": "You can visualize the invisible.", "Bodily": "You turn thoughts into action.", "Musical": "You sense rhythms and emotions.", "Interpersonal": "You instinctively understand others.", "Intrapersonal": "You have profound self-awareness.", "Naturalist": "You have a keen eye for patterns.", "Existential": "You are a visionary."},
        "lvl_desc": {1: "Focus: **'Survival & Stability'**.", 2: "Driven by **'Responsibility'**.", 3: "Value **'Contribution'**.", 4: "Guided by **'Humanity'**.", 5: "Aligned with **'Divine Calling'**."},
        "p_title": "💊 CBMID AI Prescription", "p_danger": "⚠️ High Risk / High Potential Detected", "p_ideal": "🌟 Ideal Leader Model", "p_grow": "💡 Growing Talent", "p_desc_danger": "Exceptional talent, but trapped in survival mode.", "p_desc_ideal": "Harmony of Competence and Conscience.", "p_desc_grow": "Growing steadily with sincerity."
    }
}

ARCHETYPE_NOUNS_RAW = {"Linguistic": "Storyteller", "Logical": "Strategist", "Spatial": "Architect", "Bodily": "Pioneer", "Musical": "Maestro", "Interpersonal": "Mediator", "Intrapersonal": "Philosopher", "Naturalist": "Guardian", "Existential": "Visionary"}
CONSCIENCE_ADJECTIVES_RAW = {1: "Survival", 2: "Responsible", 3: "Contributing", 4: "Humanitarian", 5: "Divine"}
MI_ORDER = ["Linguistic", "Logical", "Spatial", "Bodily", "Musical", "Interpersonal", "Intrapersonal", "Naturalist", "Existential"]

# ==========================================
# 3. 로직 및 분석 (안전한 파일 로더 적용)
# ==========================================
def load_data_safe(file):
    """
    파일을 바이트 스트림으로 읽어서 pandas로 변환 (커서 오류 및 인코딩 문제 해결)
    """
    if file is None: return None
    
    # [핵심] 파일 포인터를 무조건 처음으로 되돌림
    file.seek(0)
    
    try:
        # 파일 내용을 바이트로 읽음 (이 시점에서 스트림 소비)
        bytes_data = file.read()
        
        # 1차 시도: utf-8
        try:
            return pd.read_csv(BytesIO(bytes_data), encoding='utf-8')
        except UnicodeDecodeError:
            # 2차 시도: cp949 (한글 윈도우)
            return pd.read_csv(BytesIO(bytes_data), encoding='cp949')
    except Exception as e:
        st.error(f"❌ 파일 읽기 실패: {e}")
        return None

def analyze_data(df, lang):
    results = []
    cols = list(df.columns)
    name_idx = next((i for i, c in enumerate(cols) if "name" in c.lower() or "성함" in c), -1)
    crisis_idx = next((i for i, c in enumerate(cols) if "crisis" in c.lower() or "위기" in c), -1)
    if name_idx == -1 or crisis_idx == -1: return []
    
    potential_cols = cols[name_idx+1 : crisis_idx]
    mi_cols = [c for c in potential_cols if c.strip()[0].isdigit()]
    
    t = TEXT[lang]

    for idx, row in df.iterrows():
        scores = {}
        curr = 0
        for mi in MI_ORDER:
            if curr >= len(mi_cols): scores[mi] = 0; continue
            chunk = mi_cols[curr:curr+5]
            val_sum = 0
            for c in chunk:
                try: val_sum += int(str(row[c]).split()[0])
                except: pass
            scores[mi] = min(val_sum, 25)
            curr += 5
            
        top1 = sorted(scores.items(), key=lambda x: x[1], reverse=True)[0]
        ans = str(row[cols[crisis_idx]])
        lvl = 0
        if "1." in ans or "Survival" in ans or "생존" in ans: lvl = 1
        elif "2." in ans or "Responsibility" in ans or "책임" in ans: lvl = 2
        elif "3." in ans or "Contribution" in ans or "공헌" in ans: lvl = 3
        elif "4." in ans or "Humanity" in ans or "인류애" in ans: lvl = 4
        elif "5." in ans or "Divinity" in ans or "소명" in ans: lvl = 5
        
        raw_adj = CONSCIENCE_ADJECTIVES_RAW.get(lvl, "Shadow")
        raw_noun = ARCHETYPE_NOUNS_RAW.get(top1[0], "Explorer")
        
        adj = t["adjectives"].get(raw_adj, raw_adj)
        noun = t["archetypes"].get(raw_noun, raw_noun)
        
        archetype = f"{adj} {noun}"
        name = str(row[cols[name_idx]]).strip()
        
        results.append({
            "Name": name, "Archetype": archetype, "Level": lvl, 
            "Scores": scores, "Top1_Score": top1[1], "Top1_Raw": top1[0]
        })
    return results

# ==========================================
# 4. 화면 구성 (UI)
# ==========================================

st.sidebar.title("🧬 CBMID Engine")
language = st.sidebar.radio("Language / 언어", ["English", "KR"], index=0)
t = TEXT[language]

st.sidebar.info(f"System Ready (v3.2)")

uploaded_files = st.sidebar.file_uploader(t['upload_label'], accept_multiple_files=True, type="csv", key="csv_uploader")

all_users = []
if uploaded_files:
    for file in uploaded_files:
        df = load_data_safe(file) # 안전한 로더 사용
        if df is not None:
            all_users.extend(analyze_data(df, language))

st.title(t['title'])
st.markdown(f"### {t['subtitle']}")

if not all_users:
    st.info(t['warn_upload'])
else:
    tab1, tab2 = st.tabs([t['tab1'], t['tab2']])
    
    with tab1:
        st.subheader(f"{t['analysis_header']} {len(all_users)} {t['unit_person']}")
        plot_df = pd.DataFrame(all_users)
        
        np.random.seed(42)
        plot_df['X_J'] = plot_df['Top1_Score'] + np.random.uniform(-0.5, 0.5, len(plot_df))
        plot_df['Y_J'] = plot_df['Level'] + np.random.uniform(-0.15, 0.15, len(plot_df))
        
        fig, ax = plt.subplots(figsize=(15, 11))
        ax.grid(True, linestyle='--', alpha=0.3)
        
        colors = []
        for l in plot_df['Level']:
            if l==5: colors.append('#8E44AD')
            elif l==4: colors.append('#3498DB')
            elif l==3: colors.append('#2ECC71')
            elif l==2: colors.append('#F1C40F')
            elif l==1: colors.append('#E74C3C')
            else: colors.append('#34495E')
            
        ax.scatter(plot_df['X_J'], plot_df['Y_J'], s=400, c=colors, alpha=0.85, edgecolors='black')
        
        ax.set_title(t['matrix_title'], fontsize=20, weight='bold', pad=20)
        zone_font = {'fontsize': 16, 'weight': 'bold', 'bbox': dict(facecolor='white', alpha=0.8, edgecolor='gray', boxstyle='round,pad=0.5')}
        
        ax.text(29.8, 5.8, t['ideal'], color='green', ha='right', va='top', **zone_font)
        ax.text(29.8, 0.2, t['danger'], color='red', ha='right', va='bottom', **zone_font)
        ax.text(-3, 5.8, t['good'], color='blue', ha='left', va='top', **zone_font)
        ax.text(-3, 0.2, t['potential'], color='#E67E22', ha='left', va='bottom', **zone_font)
        
        ax.axhline(y=3, color='gray', alpha=0.3); ax.axvline(x=15, color='gray', alpha=0.3)
        ax.set_xlabel(t['x_label'], fontsize=14); ax.set_ylabel(t['y_label'], fontsize=14)
        ax.set_ylim(0, 6); ax.set_xlim(-4, 30)
        ax.set_xticks([0, 5, 10, 15, 20, 25]); ax.set_xticklabels(['0', '5', '10', '15', '20', '25 (Max)'])
        ax.set_yticks([1, 2, 3, 4, 5]); ax.set_yticklabels(['Lvl 1', 'Lvl 2', 'Lvl 3', 'Lvl 4', 'Lvl 5'])

        plot_df = plot_df.sort_values(by='X_J')
        for i, row in enumerate(plot_df.itertuples()):
            name = str(row.Name)
            x, y = row.X_J, row.Y_J
            txt_color, weight, prefix = 'black', 'normal', ""
            off_x, off_y, ha = 0, 0.35 if i%2==0 else -0.45, 'center'
            
            if 'Lise' in name or 'Jun' in name: off_y, ha = 0.5, 'center'
            elif 'Ann' in name: txt_color, weight = '#E67E22', 'bold'; off_x, off_y, ha = 0.6, 0.4, 'left'
            elif 'Mathfinder' in name: txt_color, weight = 'black', 'bold'; off_x, off_y, ha = 0.8, -0.2, 'left'
            elif 'ped0' in name.lower(): txt_color, weight, prefix = 'red', 'bold', "[!] "; off_x, off_y, ha = -0.8, 0, 'right'
            elif 'HSW' in name: txt_color, weight = '#8E44AD', 'bold'; off_y = 0.45
            elif 'Nami' in name: off_x, off_y, ha = 0, -0.5, 'center' 
                
            ax.text(x+off_x, y+off_y, prefix+name, color=txt_color, weight=weight, ha=ha, fontsize=11,
                    bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=1.5))
        
        st.pyplot(fig)
        
        fn = "CBMID_Chart_EN.png" if language == "English" else "CBMID_Chart_KR.png"
        img = BytesIO()
        fig.savefig(img, format='png', dpi=150, bbox_inches='tight')
        st.download_button(label=t['btn_download'], data=img, file_name=fn, mime="image/png")

    with tab2:
        user_list = [u['Name'] for u in all_users]
        selected = st.selectbox(t['select_user'], user_list)
        target = next(u for u in all_users if u['Name'] == selected)
        
        col1, col2 = st.columns([1, 2])
        with col1:
            fig_r, ax_r = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
            scores = target['Scores']
            val = [scores[mi] for mi in MI_ORDER]; val += val[:1]
            ang = [n/9*2*np.pi for n in range(9)]; ang += ang[:1]
            lc = '#333333' if 'ped0' in target['Name'].lower() else '#4A90E2'
            ax_r.plot(ang, val, color=lc, linewidth=2)
            ax_r.fill(ang, val, color=lc, alpha=0.2)
            ax_r.set_ylim(0, 25); ax_r.set_xticks(ang[:-1])
            
            if language == "KR": ax_r.set_xticklabels(["언어", "논리", "공간", "신체", "음악", "대인", "성찰", "자연", "실존"], size=9, weight='bold')
            else: ax_r.set_xticklabels(["Ling", "Logic", "Spat", "Body", "Music", "Inter", "Intra", "Natur", "Exist"], size=9, weight='bold')
            
            ax_r.set_title(target['Archetype'], y=1.1, size=15, weight='bold')
            st.pyplot(fig_r)
            
        with col2:
            d = t 
            top1_raw = target['Top1_Raw']
            top1_display = t['mi_names'].get(top1_raw, top1_raw)
            lvl = target['Level']
            
            st.markdown(f"## 🧬 {target['Archetype']}")
            st.info(f"**{t['rpt_top_int']}:** {top1_display} ({target['Top1_Score']}/25) | **{t['rpt_level']}:** {lvl}")
            
            st.markdown(f"### {t['h_superpower']}")
            st.write(d["int_desc"].get(top1_raw, "Unique Talent"))
            
            st.markdown(f"### {t['h_focus']}")
            st.write(d["lvl_desc"].get(lvl, "Unknown Status"))
            
            st.markdown(f"### {t['h_roadmap']}")
            st.markdown(f"#### {t['p_title']}")
            if target['Level'] <= 1 and target['Top1_Score'] >= 20:
                st.error(t['p_danger']); st.write(t['p_desc_danger'])
                if language == "KR":
                    st.warning("🔻 **Step 1: 그라운딩** - 생존 기반 마련 및 기술 수익화.\n\n🔻 **Step 2: 연결** - 커뮤니티 참여 및 심리적 지지.\n\n🔻 **Step 3: 도약** - 안정 후 철학과 비전 실현.")
                else:
                    st.warning("🔻 **Step 1: Grounding** - Secure economic foundation.\n\n🔻 **Step 2: Connection** - Join support communities.\n\n🔻 **Step 3: Leap** - Unleash vision after stability.")
            elif target['Level'] >= 4:
                st.success(t['p_ideal']); st.write(t['p_desc_ideal'])
                if language == "KR":
                    st.write("🚀 **Step 1: 확장** - 시스템과 문화 구축.\n\n🚀 **Step 2: 멘토링** - 후배 인재 양성.\n\n🚀 **Step 3: 유산** - 철학과 가치 전수.")
                else:
                    st.write("🚀 **Step 1: Expansion** - Build systems & culture.\n\n🚀 **Step 2: Mentoring** - Guide others.\n\n🚀 **Step 3: Legacy** - Pass on philosophy.")
            else:
                st.info(t['p_grow']); st.write(t['p_desc_grow'])
                if language == "KR":
                    st.write("🔹 **Step 1: 심화** - 강점 지능 전문성 강화.\n\n🔹 **Step 2: 융합** - 보조 지능과 결합.\n\n🔹 **Step 3: 기여** - 타인을 돕는 경험.")
                else:
                    st.write("🔹 **Step 1: Deepening** - Master top intelligence.\n\n🔹 **Step 2: Convergence** - Combine strengths.\n\n🔹 **Step 3: Contribution** - Help others.")