# 🎭 Shatar - Arabic Poetry Generator

A beautiful Streamlit web application that generates authentic Arabic poetry using AI. Create classical and modern Arabic poems with traditional poetic meters (البحور) using either Anthropic Claude or OpenAI GPT models.

![Poetry Generator](https://img.shields.io/badge/Language-Arabic-green) ![AI-Powered](https://img.shields.io/badge/AI-Powered-blue) ![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-red)

## ✨ Features

- 🎨 **Generate Arabic Poetry** on any topic
- 📜 **8 Classical Arabic Meters** (البحور الشعرية)
- 🎯 **Two Styles**: Classical (كلاسيكي) and Modern (حديث)
- 🤖 **Dual AI Support**: Choose between Anthropic Claude or OpenAI GPT
- 📱 **Responsive Design** for mobile and desktop
- 📥 **Download Poems** as text files
- 🎨 **Beautiful Typography** with Arabic font support

## 🚀 Demo

Try the live demo: [Coming Soon]

## 📋 Prerequisites

- Python 3.8+
- API key from either:
  - [Anthropic](https://console.anthropic.com) (Claude)
  - [OpenAI](https://platform.openai.com) (GPT)

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/shatar-arabic-poetry.git
cd shatar-arabic-poetry
```

### 2. Create Virtual Environment
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Keys
Create `.streamlit/secrets.toml`:
```toml
# Add one or both API keys
ANTHROPIC_API_KEY = "your-anthropic-api-key"
OPENAI_API_KEY = "your-openai-api-key"
```

### 5. Run the Application
```bash
streamlit run Shatar.py
```

The app will open in your browser at `http://localhost:8501`

## 🎯 Usage

1. **Enter Topic**: Write your poem's theme (e.g., الحب، الطبيعة، الوطن)
2. **Select Meter**: Choose from 8 classical Arabic meters
3. **Pick Style**: Classical or Modern poetry style
4. **Set Verses**: Choose 2-10 verses
5. **Choose AI**: Select Anthropic Claude or OpenAI GPT
6. **Generate**: Click "أنشئ القصيدة" to create your poem
7. **Download**: Save your poem as a text file

## 📜 Supported Arabic Meters (البحور)

| Arabic Name | Transliteration | Pattern |
|-------------|-----------------|---------|
| البسيط | Al-Basit | مُسْتَفْعِلُنْ فَاعِلُنْ مُسْتَفْعِلُنْ فَعِلُنْ |
| الطويل | At-Taweel | فَعُولُنْ مَفَاعِيلُنْ فَعُولُنْ مَفَاعِلُنْ |
| الوافر | Al-Wafer | مُفَاعَلَتُنْ مُفَاعَلَتُنْ فَعُولُنْ |
| الكامل | Al-Kamel | مُتَفَاعِلُنْ مُتَفَاعِلُنْ مُتَفَاعِلُنْ |
| الهزج | Al-Hazaj | مَفَاعِيلُنْ مَفَاعِيلُنْ |
| الرجز | Ar-Rajaz | مُسْتَفْعِلُنْ مُسْتَفْعِلُنْ مُسْتَفْعِلُنْ |
| المتقارب | Al-Mutaqareb | فَعُولُنْ فَعُولُنْ فَعُولُنْ فَعُولُنْ |
| الرمل | Ar-Ramal | فَاعِلاتُنْ فَاعِلاتُنْ فَاعِلاتُنْ |

## 🤖 AI Models Used

- **Anthropic Claude**: `claude-3-5-sonnet-20241022`
- **OpenAI GPT**: `gpt-4o`

## 💰 Cost Estimation

Approximate cost per poem generation:
- **Anthropic Claude**: ~$0.005 (0.5 cents)
- **OpenAI GPT**: ~$0.003 (0.3 cents)

## 🌐 Deployment

### Deploy on Streamlit Cloud

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Create new app from your GitHub repository
4. Add secrets in app settings:
   ```toml
   ANTHROPIC_API_KEY = "your-key"
   OPENAI_API_KEY = "your-key"
   ```
5. Deploy!

### Deploy on Heroku

1. Create `Procfile`:
   ```
   web: streamlit run Shatar.py --server.port=$PORT --server.address=0.0.0.0
   ```
2. Set environment variables in Heroku dashboard
3. Deploy from GitHub

## 🔧 Technical Details

### Built With
- **Frontend**: Streamlit
- **AI APIs**: Anthropic Claude API, OpenAI API
- **Language**: Python 3.8+
- **Styling**: Custom CSS for Arabic typography

### Project Structure
```
shatar-arabic-poetry/
├── Shatar.py                 # Main application
├── requirements.txt          # Dependencies
├── README.md                # Documentation
├── .gitignore               # Git ignore rules
├── .streamlit/
│   └── secrets.toml         # API keys (local only)
└── test_api.py              # API testing script
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Traditional Arabic poetry meters and rules
- Streamlit community for the amazing framework
- Anthropic and OpenAI for powerful language models

## 📞 Support

If you encounter any issues or have questions:
- Open an [Issue](https://github.com/yourusername/shatar-arabic-poetry/issues)
- Contact: [ahmedsabri85@gmail.com]

---

**Made with ❤️ for Arabic poetry lovers**
