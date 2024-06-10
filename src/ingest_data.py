from stormglass_api import get_wave_data
from database import SessionLocal, SurfData
from datetime import datetime

# Coordenadas das principais praias, incluindo Barra da Tijuca, Rio de Janeiro
beaches = [
    {'name': 'Barra da Tijuca', 'lat': -23.0000, 'lng': -43.3657},
    # Adicione outras praias aqui, se necessário
]

def ingest_data():
    session = SessionLocal()
    for beach in beaches:
        wave_data = get_wave_data(beach['lat'], beach['lng'])
        
        surf_data = SurfData(
            beach=beach['name'],
            timestamp=datetime.utcnow(),
            wave_height=wave_data['hours'][0]['waveHeight']['noaa'],
            temperature=wave_data['hours'][0].get('airTemperature', {}).get('noaa'),
            wind_speed=wave_data['hours'][0].get('windSpeed', {}).get('noaa')
        )
        
        session.add(surf_data)
    session.commit()
    session.close()

if __name__ == '__main__':
    ingest_data()
