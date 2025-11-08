# Yahoo Finance Data Pipeline 📈

Un pipeline completo para extraer, procesar y analizar datos financieros de Yahoo Finance, optimizado para ejecución en Google Colab y Termux/Android.

![Python](https://img.shields.io/badge/python-3.8%2B-blue)
![Platform](https://img.shields.io/badge/platform-colab%20%7C%20termux-success)
![License](https://img.shields.io/badge/license-MIT-green)

## 🚀 Características

- **Extracción de datos**: Obtención de datos históricos en tiempo real de Yahoo Finance
- **Procesamiento avanzado**: Cálculo de indicadores técnicos (RSI, SMA, Volatilidad)
- **Múltiples formatos**: Exportación a CSV, JSON y TXT
- **Visualización**: Gráficos interactivos con Plotly y Matplotlib
- **Cloud Ready**: Integración con Google Drive y preparación para servicios cloud
- **Multiplataforma**: Ejecutable en Google Colab y Termux/Android

## 📊 Indicadores Calculados

- Precio de cierre, apertura, máximo y mínimo
- Retornos diarios
- Medias móviles (SMA 20, SMA 50)
- Volatilidad (20 días)
- RSI (14 períodos)
- Volumen de trading

## 🛠️ Instalación Rápida

### Google Colab (Recomendado)
```python
# Ejecutar en celdas separadas
!git clone https://github.com/tu-usuario/yahoo-finance-pipeline.git
%cd yahoo-finance-pipeline

# Instalar dependencias
!pip install yfinance pandas numpy plotly seaborn -q

# Ejecutar pipeline
!python main.py
Termux (Android)
bash
git clone https://github.com/tu-usuario/yahoo-finance-pipeline.git
cd yahoo-finance-pipeline
pkg install python-pip
pip install yfinance pandas numpy python-dotenv pyyaml schedule
python main.py
📁 Estructura del Proyecto
text
yahoo_finance_cloud/
├── src/
│   ├── data_fetcher.py          # Extracción de datos de Yahoo Finance
│   ├── data_processor.py        # Procesamiento y transformación
│   ├── cloud_uploader.py        # Subida a servicios cloud
│   └── colab_utils.py           # Utilidades para Google Colab
├── data/
│   ├── raw/                     # Datos brutos
│   ├── processed/               # Datos procesados
│   └── exports/                 # Archivos de exportación
├── outputs/                     # Resultados del pipeline
├── notebooks/                   # Jupyter notebooks de análisis
├── config/                      # Archivos de configuración
└── scripts/                     # Scripts de automatización
🎯 Uso Básico
python
from src.data_fetcher import YahooDataFetcher
from src.data_processor import DataProcessor

# Obtener datos
fetcher = YahooDataFetcher()
symbols = ["AAPL", "GOOGL", "MSFT", "TSLA"]
raw_data = fetcher.fetch_stock_data(symbols)

# Procesar y analizar
processor = DataProcessor()
processed_data = processor.clean_and_transform(raw_data)

# Exportar resultados
exports = processor.export_to_text(processed_data)
📈 Símbolos Preconfigurados
El pipeline incluye análisis automático para:

AAPL (Apple)

GOOGL (Alphabet)

MSFT (Microsoft)

TSLA (Tesla)

AMZN (Amazon)

META (Meta Platforms)

NVDA (NVIDIA)

🔧 Configuración
Edita config.yaml para personalizar:

yaml
symbols:
  - "AAPL"
  - "GOOGL"
period: "6mo"
interval: "1d"
exports:
  formats: ["csv", "json", "txt"]
  keep_local: true
📤 Exportación de Resultados
Google Colab
python
# Descargar ZIP con todos los resultados
from google.colab import files
files.download('/content/finance_data_export.zip')

# Guardar en Google Drive
from src.colab_utils import ColabUtils
ColabUtils().save_to_drive()
Termux
bash
# Los archivos se guardan automáticamente en:
./outputs/csv/    # Datos completos en CSV
./outputs/json/   # Datos en formato JSON
./outputs/txt/    # Resúmenes ejecutivos
📊 Ejemplo de Salida
Archivo de Resumen (TXT)
text
YAHOO FINANCE DATA EXPORT
=========================
SYMBOL: AAPL
EXPORT TIME: 2024-01-15 14:30:25
DATA POINTS: 126
PERIOD: 2023-07-01 to 2023-12-31

PRICE INFORMATION:
------------------
LATEST PRICE: $185.25
DAILY CHANGE: +1.25%
VOLUME: 58,425,000

TECHNICAL INDICATORS:
---------------------
SMA 20: $182.45
SMA 50: $178.90
VOLATILITY (20d): 2.45%
RSI: 58.3
🤝 Contribución
¡Las contribuciones son bienvenidas! Por favor:

Fork el proyecto

Crea una rama para tu feature (git checkout -b feature/AmazingFeature)

Commit tus cambios (git commit -m 'Add some AmazingFeature')

Push a la rama (git push origin feature/AmazingFeature)

Abre un Pull Request

📝 Licencia
Distribuido bajo la Licencia MIT. Ver LICENSE para más información.

📞 Soporte
Si encuentras algún problema o tienes preguntas:

Abre un issue

Consulta la documentación

Revisa los ejemplos

¿Te gusta este proyecto? ⭐ Dale una estrella en GitHub para apoyar su desarrollo!
