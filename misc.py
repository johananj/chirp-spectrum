# def cs_play(r = 0.99):
#     f = [5, 10, 15]
#     a = [0.95, 0.96, 0.97]
#     x = np.zeros((500,))
#     for fc, ac in zip(f, a):
#         xc, _ = generate_signal(fm = fc, a = ac)
#         x = x + xc
    
#     mag, ph = cs_basic(x, r = r, plotting = False)
    
#     xi  = np.zeros((500,))
#     for fb in np.linspace(0,25,6):
#         fb = int(fb)
#         xc, _ = generate_signal(fm = fb, pd = ph[fb])
#         xi = xi + xc
    
#     fig, axs = plt.subplots(2, 2)
#     fig.set_figwidth(12)
#     fig.set_figheight(8)
#     axs[0,0].plot(x)
#     axs[0,0].title.set_text('Input')
#     # axs[0].set_xlim(0,max_freq)
#     # axs[0].set_ylim(0,max_val)
#     axs[0,1].plot(xi)
#     axs[0,1].title.set_text('Reconstructed')
#     axs[1,0].stem(mag)
#     axs[1,0].title.set_text('Magnitude Spectrum')
#     axs[1,1].stem(ph)
#     axs[1,1].title.set_text('Phase Spectrum')
#     plt.show()

# r_s = widgets.FloatSlider(value = 1, min = 0.75, max = 1.25, step=0.01)
# widgets.interact(cs_play, r=r_s)