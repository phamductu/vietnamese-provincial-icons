import matplotlib.pyplot as plt
import geopandas as gpd
from vietnamese_formatter import vietnamese2id 

NUM_PROVINCES = 63

if __name__ == '__main__':
    gdf = gpd.read_file('diaphantinh.json')
    for gid in range(1, NUM_PROVINCES+1):
        cur = gdf[gdf.gid == gid]
        province = str(cur.ten_tinh).split('\n')[0][2:].strip()
        fig, ax = plt.subplots(figsize=(15,15))
        ax.set_axis_off()
        ax.margins(0)
        plt.tight_layout()
        fig.patch.set_alpha(0)
        ax = cur.plot(figsize=(15,15), color="black", ax=ax, aspect='equal')
        plt.savefig('provinces/' + vietnamese2id(province) + '.svg', format='svg', dpi=1200)
