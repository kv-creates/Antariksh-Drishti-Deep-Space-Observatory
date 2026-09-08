import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np, os
out='docs/images'
os.makedirs(out, exist_ok=True)
# 1 hero orbit
fig,ax=plt.subplots(figsize=(10,4),facecolor='#0b0f19')
ax.set_facecolor('#0b0f19')
t=np.linspace(0,2*np.pi,200)
ax.plot(np.cos(t)*7, np.sin(t)*7, color='#60a5fa', lw=2, label='LEO 7000km')
ax.plot(np.cos(t)*10, np.sin(t)*10, color='#34d399', lw=1.5, ls='--', label='MEO')
ax.set_title('Antariksh-Drishti Constellation Orbits', color='white')
ax.legend(facecolor='#111827', labelcolor='white')
ax.tick_params(colors='white')
fig.tight_layout(); fig.savefig(f'{out}/hero-orbits.png', dpi=150, facecolor=fig.get_facecolor()); plt.close(fig)
# 2 lightcurve
fig,ax=plt.subplots(figsize=(10,3.5),facecolor='white')
time=np.linspace(0,10,500)
flux=[1-0.012 if 4.9<x<5.1 else 1 for x in time]
ax.plot(time,flux,color='#0b3d91')
ax.set_title('Exoplanet Transit Light Curve (depth 1.2%)')
ax.set_xlabel('days'); ax.set_ylabel('normalized flux')
fig.tight_layout(); fig.savefig(f'{out}/lightcurve.png', dpi=150); plt.close(fig)
# 3 HR diagram
fig,ax=plt.subplots(figsize=(6,4))
np.random.seed(0)
temp=np.random.normal(5800,1200,300)
lum=np.random.normal(0,1,300)
ax.scatter(temp,lum,c=lum,cmap='plasma',s=12)
ax.invert_xaxis(); ax.set_xlabel('Teff K'); ax.set_ylabel('log L')
ax.set_title('H-R Diagram Target Sample')
fig.tight_layout(); fig.savefig(f'{out}/hr-diagram.png', dpi=150); plt.close(fig)
# 4 scheduler gantt
fig,ax=plt.subplots(figsize=(10,3))
ax.broken_barh([(0,60),(65,30),(100,45)],(5,4),facecolors='#0b3d91')
ax.set_yticks([7]); ax.set_yticklabels(['JWST-like']); ax.set_xlabel('minutes')
ax.set_title('Observation Schedule Gantt')
fig.tight_layout(); fig.savefig(f'{out}/schedule-gantt.png', dpi=150); plt.close(fig)
# 5 SNR heatmap
fig,ax=plt.subplots(figsize=(6,4))
data=np.random.rand(10,10)
im=ax.imshow(data,cmap='viridis')
fig.colorbar(im,ax=ax,label='SNR')
ax.set_title('Detector SNR Heatmap')
fig.tight_layout(); fig.savefig(f'{out}/snr-heatmap.png', dpi=150); plt.close(fig)
# 6 architecture png (simple block)
fig,ax=plt.subplots(figsize=(10,2.5),facecolor='#0f172a')
ax.set_facecolor('#0f172a'); ax.axis('off')
for i,lab in enumerate(['TLE','SGP4','Scheduler','Imager','Photometry']):
    ax.add_patch(plt.Rectangle((i*2+0.2,0.4),1.6,0.6,facecolor='#1e3a8a',edgecolor='white'))
    ax.text(i*2+1.0,0.7,lab,ha='center',va='center',color='white',fontsize=9)
    if i<4: ax.arrow(i*2+1.8,0.7,i*2+2.2- (i*2+1.8),0,head_width=0.08,color='white')
ax.set_xlim(0,10); ax.set_ylim(0,1.2); ax.set_title('Pipeline',color='white')
fig.tight_layout(); fig.savefig(f'{out}/pipeline.png', dpi=150, facecolor=fig.get_facecolor()); plt.close(fig)
print('visuals done')
