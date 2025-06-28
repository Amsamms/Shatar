import streamlit as st
import anthropic
import openai
import os

# Page configuration
st.set_page_config(
    page_title="مولد الشعر العربي - Shatar",
    page_icon="🎭",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://github.com/yourusername/shatar-arabic-poetry',
        'Report a bug': 'https://github.com/yourusername/shatar-arabic-poetry/issues',
        'About': """
        # Shatar - Arabic Poetry Generator
        Generate beautiful Arabic poetry using AI
        
        **Features:**
        - 8 Classical Arabic meters
        - Anthropic Claude & OpenAI GPT support
        - Download generated poems
        """
    }
)

class ArabicPoetryGenerator:
    def __init__(self, anthropic_key: str = None, openai_key: str = None):
        self.anthropic_client = None
        self.openai_client = None
        
        if anthropic_key:
            self.anthropic_client = anthropic.Anthropic(api_key=anthropic_key)
        if openai_key:
            self.openai_client = openai.OpenAI(api_key=openai_key)
        
        self.meters = {
            "البسيط": "مُسْتَفْعِلُنْ فَاعِلُنْ مُسْتَفْعِلُنْ فَعِلُنْ",
            "الطويل": "فَعُولُنْ مَفَاعِيلُنْ فَعُولُنْ مَفَاعِلُنْ",
            "الوافر": "مُفَاعَلَتُنْ مُفَاعَلَتُنْ فَعُولُنْ",
            "الكامل": "مُتَفَاعِلُنْ مُتَفَاعِلُنْ مُتَفَاعِلُنْ",
            "الهزج": "مَفَاعِيلُنْ مَفَاعِيلُنْ",
            "الرجز": "مُسْتَفْعِلُنْ مُسْتَفْعِلُنْ مُسْتَفْعِلُنْ",
            "المتقارب": "فَعُولُنْ فَعُولُنْ فَعُولُنْ فَعُولُنْ",
            "الرمل": "فَاعِلاتُنْ فَاعِلاتُنْ فَاعِلاتُنْ"
        }

    def generate_poem(self, theme: str, meter: str = "البسيط", num_verses: int = 4, style: str = "classical", api_provider: str = "anthropic"):
        if meter not in self.meters:
            meter = "البسيط"
        
        style_instruction = "بأسلوب شعري حديث ومعاصر" if style == "modern" else "بأسلوب شعري كلاسيكي فصيح"
        
        prompt = f"""اكتب قصيدة عربية جميلة {style_instruction}

الموضوع: {theme}
البحر الشعري: {meter}
التفعيلة: {self.meters[meter]}
عدد الأبيات: {num_verses}

شروط مهمة:
- التزم بالوزن الشعري بدقة تامة
- استخدم قافية موحدة
- اجعل المعنى واضحاً وجميلاً
- تجنب التعقيد اللغوي المفرط
- اكتب القصيدة مباشرة بدون مقدمات أو تعليقات

القصيدة:"""

        try:
            if api_provider == "anthropic" and self.anthropic_client:
                response = self.anthropic_client.messages.create(
                    model="claude-3-5-sonnet-20241022",
                    max_tokens=1000,
                    temperature=0.8,
                    messages=[{"role": "user", "content": prompt}]
                )
                poem_text = response.content[0].text.strip()
                return True, poem_text
                
            elif api_provider == "openai" and self.openai_client:
                response = self.openai_client.chat.completions.create(
                    model="gpt-4o",  # Using GPT-4o (latest model)
                    max_tokens=1000,
                    temperature=0.8,
                    messages=[{"role": "user", "content": prompt}]
                )
                poem_text = response.choices[0].message.content.strip()
                return True, poem_text
            
            else:
                return False, f"خطأ: {api_provider} غير متاح أو لم يتم تكوينه"
            
        except anthropic.APIError as e:
            return False, f"خطأ في Anthropic API: {str(e)}"
        except openai.APIError as e:
            return False, f"خطأ في OpenAI API: {str(e)}"
        except Exception as e:
            return False, f"خطأ: {str(e)}"

# App Title
st.title("🎭 مولد الشعر العربي")
st.markdown("---")

# Get API keys from Streamlit secrets or environment variables
anthropic_key = None
openai_key = None
api_keys_available = False

try:
    # Try Streamlit secrets first
    anthropic_key = st.secrets.get("ANTHROPIC_API_KEY")
    openai_key = st.secrets.get("OPENAI_API_KEY")
    
    if anthropic_key or openai_key:
        api_keys_available = True
        # Production: Clean interface - no API key status messages
    else:
        st.warning("⚠️ لم يتم العثور على مفاتيح API في الإعدادات")
        
except Exception as e:
    try:
        # Try environment variables
        anthropic_key = os.getenv("ANTHROPIC_API_KEY")
        openai_key = os.getenv("OPENAI_API_KEY")
        
        if anthropic_key or openai_key:
            api_keys_available = True
        else:
            api_keys_available = False
            st.error("❌ لم يتم العثور على مفاتيح API. يرجى إعداد ANTHROPIC_API_KEY أو OPENAI_API_KEY")
    except:
        api_keys_available = False
        st.error("❌ خطأ في تحميل مفاتيح API.")

# Main interface
if api_keys_available:
    # User input
    user_prompt = st.text_area(
        "اكتب موضوع القصيدة:",
        placeholder="مثال: الحب، الطبيعة، الوطن، الصداقة...",
        height=100
    )
    
    # Options in columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        meter = st.selectbox(
            "البحر الشعري:",
            ["البسيط", "الطويل", "الوافر", "الكامل", "الهزج", "الرجز", "المتقارب", "الرمل"]
        )
    
    with col2:
        style = st.selectbox(
            "الأسلوب:",
            ["classical", "modern"],
            format_func=lambda x: "كلاسيكي" if x == "classical" else "حديث"
        )
    
    with col3:
        num_verses = st.number_input(
            "عدد الأبيات:",
            min_value=2,
            max_value=10,
            value=4
        )
    
    with col4:
        # API Provider selection
        available_providers = []
        if anthropic_key:
            available_providers.append("anthropic")
        if openai_key:
            available_providers.append("openai")
            
        api_provider = st.selectbox(
            "مزود الخدمة:",
            available_providers,
            format_func=lambda x: "Anthropic (Claude)" if x == "anthropic" else "OpenAI (GPT)"
        )
    
    # Generate button
    if st.button("🎨 أنشئ القصيدة", type="primary", use_container_width=True):
        if user_prompt.strip():
            with st.spinner("جاري إنشاء القصيدة..."):
                try:
                    poet = ArabicPoetryGenerator(anthropic_key=anthropic_key, openai_key=openai_key)
                    success, result = poet.generate_poem(
                        theme=user_prompt.strip(),
                        meter=meter,
                        num_verses=num_verses,
                        style=style,
                        api_provider=api_provider
                    )
                    
                    if success:
                        st.markdown("### 📜 القصيدة:")
                        # Show which API was used
                        provider_name = "Anthropic (Claude)" if api_provider == "anthropic" else "OpenAI (GPT)"
                        st.info(f"🤖 تم إنشاؤها باستخدام: {provider_name}")
                        
                        # Display poem in a beautiful container
                        st.markdown(
                            f"""
                            <div style="
                                background-color: #f8f9fa;
                                border-right: 4px solid #007bff;
                                padding: 20px;
                                margin: 10px 0;
                                border-radius: 5px;
                                font-family: 'Amiri', serif;
                                font-size: 18px;
                                line-height: 2;
                                text-align: right;
                                direction: rtl;
                            ">
                            {result.replace(chr(10), '<br>')}
                            </div>
                            """,
                            unsafe_allow_html=True
                        )
                        
                        # Download button
                        st.download_button(
                            label="📥 تحميل القصيدة",
                            data=result,
                            file_name=f"قصيدة_{user_prompt[:20]}.txt",
                            mime="text/plain"
                        )
                    else:
                        st.error(f"❌ {result}")
                        
                except Exception as e:
                    st.error(f"❌ خطأ غير متوقع: {str(e)}")
        else:
            st.warning("⚠️ يرجى إدخال موضوع للقصيدة")

else:
    st.info("⚠️ التطبيق غير جاهز - يرجى إعداد مفتاح API واحد على الأقل")

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>مولد الشعر العربي باستخدام الذكاء الاصطناعي</div>",
    unsafe_allow_html=True
)