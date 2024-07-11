import tkinter as tk
import numpy as np
import os
import shutil
import matplotlib.pyplot as plt
import runge4 

################ Widget's Gui ################

# Global variables for widgets
en1_dt = None
en2_t_final = None
en3_ic_xi = None
en4_ic_xf = None
en5_ic_amount_x = None
en6_ic_pi = None
en7_ic_pf = None
en8_ic_amount_p = None
en9_mass = None
en10_force = None

button_save_xls = None
button_save_map = None
button_create_dir = None

label_save_current_map = None
label_save_trajectory = None
en11_file = None
en12_file = None

en13_file = None
########################################

################ Data Saving ################
def f_create_dir(dir_name):
    global label_save_trajectory,en11_file, en12_file, button_save_xls, label_save_current_map, en13_file, button_save_map, button_create_dir
    current_directory = os.getcwd()
    directory_path = os.path.join(current_directory, dir_name)
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        create_dir_window = tk.Toplevel(root) 
        create_dir_window.title("Directory Created")
        create_dir_window.geometry(f"200x80+800+200")
        label = tk.Label(create_dir_window, text=f"Directory '{dir_name}'\n\
    created successfully.")
        label.pack(padx=20, pady=20) 
    else:
        create_dir_window = tk.Toplevel(root) 
        create_dir_window.title("Directory Created")
        create_dir_window.geometry(f"200x80+800+200")
        label = tk.Label(create_dir_window, text=f"Directory '{dir_name}'\n\
    already exists.")
        label.pack(padx=20, pady=20) 
    button_create_dir.config(state=tk.DISABLED)
    en11_file.config(state='disabled')
    enable_second_widgets()

def f_save_csv(coord_mat,time_vec,dir_name):
    global label_save_trajectory,en11_file, en12_file, button_save_xls, label_save_current_map, en13_file, button_save_map, button_create_dir
    np.savetxt('trajectories.csv', coord_mat, delimiter=',')
    shutil.move('trajectories.csv', os.path.join(dir_name, os.path.basename(('trajectories.csv'))))
    np.savetxt('time.csv', time_vec, delimiter=',')
    shutil.move('time.csv', os.path.join(dir_name, os.path.basename(('time.csv'))))

    save_csv_window = tk.Toplevel(root) 
    save_csv_window.title("csv Saved")
    save_csv_window.geometry(f"200x80+800+200")
    label = tk.Label(save_csv_window, text="Trajectory and Time\n\
saved successfully.")
    label.pack(padx=20, pady=20)  
    button_save_xls.config(state=tk.DISABLED)

def f_save_map(dir_name, fig_name, fig):
    fig_name_for_save = str(fig_name)+".png"
    file_path = os.path.join(dir_name, fig_name_for_save)
    if not os.path.isfile(file_path):
        fig.savefig(fig_name_for_save)
        shutil.move(fig_name_for_save, os.path.join(dir_name, os.path.basename((fig_name_for_save))))
        save_figure_window = tk.Toplevel(root) 
        save_figure_window.title("png Saved")
        save_figure_window.geometry(f"250x80+800+200")
        label = tk.Label(save_figure_window, text=f"Figure {fig_name}\n\
    saved successfully.")
        label.pack(padx=20, pady=20)  
    else:
        create_dir_window = tk.Toplevel(root) 
        create_dir_window.title("png Saved")
        create_dir_window.geometry(f"200x80+800+200")
        label = tk.Label(create_dir_window, text=f"Figure {fig_name}\n\
    already exists.")
        label.pack(padx=20, pady=20) 
########################################

################ tk gui ################
root = tk.Tk()
root.title("Hamiltonian System Analyzer")
root.geometry("410x430")  

# time
label = tk.Label(root, text=f"Time Interval")
label.grid(row=0, column=0, padx=10, pady=5, sticky="e")
en1_dt = tk.Entry(root)
en1_dt.insert(0,0.01)
en1_dt.grid(row=0, column=1, padx=10, pady=5)

def f_time_info_window():
    time_info_window = tk.Toplevel(root) 
    time_info_window.title("Time Information")
    time_info_window.geometry(f"250x100+800+200")
    label = tk.Label(time_info_window, text="After the first test, \n\
    decrease the time interval\n\
    to verify convergence")
    label.pack(padx=20, pady=20)  
button_time_info_window = tk.Button(root, text="?", command=f_time_info_window)
button_time_info_window.grid(row=0, column=2, padx=0, pady=0, sticky="e")

label = tk.Label(root, text=f"Total Time")
label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
en2_t_final = tk.Entry(root)
en2_t_final.insert(0,7)
en2_t_final.grid(row=1, column=1, padx=10, pady=5)

# initial conditions
label = tk.Label(root, text=f"First Position")
label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
en3_ic_xi = tk.Entry(root)
en3_ic_xi.insert(0,1)
en3_ic_xi.grid(row=2, column=1, padx=10, pady=5)

label = tk.Label(root, text=f"Last Position")
label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
en4_ic_xf = tk.Entry(root)
en4_ic_xf.insert(0,5)
en4_ic_xf.grid(row=3, column=1, padx=10, pady=5)

label = tk.Label(root, text=f"Positions Amount")
label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
en5_ic_amount_x = tk.Entry(root)
en5_ic_amount_x.insert(0,5)
en5_ic_amount_x.grid(row=4, column=1, padx=10, pady=5)

label = tk.Label(root, text=f"First Momentum")
label.grid(row=5, column=0, padx=10, pady=5, sticky="e")
en6_ic_pi = tk.Entry(root)
en6_ic_pi.insert(0,1)
en6_ic_pi.grid(row=5, column=1, padx=10, pady=5)

label = tk.Label(root, text=f"Last Momentum")
label.grid(row=6, column=0, padx=10, pady=5, sticky="e")
en7_ic_pf = tk.Entry(root)
en7_ic_pf.insert(0,1)
en7_ic_pf.grid(row=6, column=1, padx=10, pady=5)

label = tk.Label(root, text=f"Momenta Amount")
label.grid(row=7, column=0, padx=10, pady=5, sticky="e")
en8_ic_amount_p = tk.Entry(root)
en8_ic_amount_p.insert(0,'1')
en8_ic_amount_p.grid(row=7, column=1, padx=10, pady=5)

label = tk.Label(root, text=f"Mass")
label.grid(row=8, column=0, padx=10, pady=5, sticky="e")
en9_mass = tk.Entry(root)
en9_mass.insert(0,'1')
en9_mass.grid(row=8, column=1, padx=10, pady=5)

label = tk.Label(root, text=f"Force Expression")
label.grid(row=9, column=0, padx=10, pady=5, sticky="e")
en10_force = tk.Entry(root)
en10_force.insert(0,'-x+(1/2)*sign(p)*abs(x)')
en10_force.grid(row=9, column=1, padx=10, pady=5)

def f_force_info_window():
    force_info_window = tk.Toplevel(root) 
    force_info_window.title("Force Information")
    force_info_window.geometry(f"400x200+800+200")
    label = tk.Label(force_info_window, text="-Arguments: x (positions), p (momenta), t (time) \n\
                     \n\
    -Pay attention to parentheses \n\
                     \n\
    -Syntax for power is ** (not ^) \n\
                     \n\
    -Allowed function notation: \n\
                     \n\
    cos, cosh, sin, sinh, arccos, arccosh, arcsin ,arcsinh, \n\
    arctan, arctan2, arctanh, exp, log, log10, sqrt, abs, sign")

    label.pack(padx=20, pady=20)    
button_force_info_window = tk.Button(root, text="?", command=f_force_info_window)
button_force_info_window.grid(row=9, column=2, padx=2, pady=2, sticky="e")

def f_continue():
    main()

button_continue = tk.Button(root, text="Choose Time Surface", command=f_continue)
button_continue.grid(row=10, column=1, padx=10, pady=5)
########################################

################ Main Function ################
def main():
    global label_save_trajectory,en11_file, en12_file, button_save_xls, label_save_current_map, en13_file, button_save_map, button_create_dir

    dt = float(en1_dt.get())
    t_final = float(en2_t_final.get())
    ic_xi = float(en3_ic_xi.get())
    ic_xf = float(en4_ic_xf.get()) 
    x_amount = int(en5_ic_amount_x.get())
    ic_pi = float(en6_ic_pi.get())
    ic_pf = float(en7_ic_pf.get()) 
    p_amount = int(en8_ic_amount_p.get())
    mass = float(en9_mass.get()) 
    force = en10_force.get()

    time_vec = np.arange(dt, t_final+dt, dt)
    time_amount = len(time_vec)

    coord_mat = np.zeros((2*x_amount*p_amount, time_amount))
   
    # initial coordinates
    ic_x_vec = np.linspace(ic_xi, ic_xf, x_amount)
    ic_p_vec = np.linspace(ic_pi, ic_pf, p_amount)
    counter = 0 
    for i in ic_x_vec:
        for j in ic_p_vec:
            coord_mat[counter,0] = i
            coord_mat[counter+x_amount*p_amount,0] = j
            counter += 1

    # time propagation by runge4
    for i in range(time_amount-1):
        time = time_vec[i]
        coord = coord_mat[:, i]
        coord_mat[:,(i+1)] = runge4.f_new_cord(lambda coord, time: runge4.f_ode(coord, time, mass, force, x_amount, p_amount), coord, time, dt)

    # Map figure and time scroller
    fig, ax = plt.subplots()
    plt.get_current_fig_manager().window.wm_geometry("700x500+800+200")
    
    def on_scroll(event):
        pos = scrollbar.get()
        idx = int(pos[0] * (len(time_vec) - 1))+1
        value_label.config(text=f"`Time Interval Sections`: {time_vec[idx]:.3f}") 
        surface_x = coord_mat[0:x_amount*p_amount,0::idx]
        surface_x_flat = surface_x.flatten()
        surface_p = coord_mat[x_amount*p_amount:,0::idx]    
        surface_p_flat = surface_p.flatten()
        ax.clear() 
        ax.scatter(surface_x_flat, surface_p_flat, s=2, c='black')
        ax.set_xlabel('x')
        ax.set_ylabel('p')
        ax.set_title('Stroboscopic Map')
        fig.canvas.draw() 
        plt.show()

    # gui for data saving and scrollbar
    def update_scroll_region():
        total_width = sum(len(str(value)) * 10 for value in time_vec)
        canvas.config(scrollregion=(0, 0, total_width, 0))

    root = tk.Tk()
    root.title("Time Surface")
    root.geometry("650x400")  

    frame = tk.Frame(root, width=600, height=50)
    frame.pack(padx=10, pady=10)

    canvas = tk.Canvas(frame, width=600, height=50)
    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame, orient='horizontal', command=canvas.xview)
    scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    canvas.configure(xscrollcommand=scrollbar.set)
    update_scroll_region()

    scrollbar.bind("<B1-Motion>", on_scroll)

    value_label = tk.Label(root, text="Time Interval Sections: non")
    value_label.pack(pady=10)

    label = tk.Label(root, text=f"Create New Directory")
    label.pack(padx=10, pady=5) 
    en11_file = tk.Entry(root)
    en11_file.insert(0,'directory_name')
    en11_file.pack(padx=10, pady=5)
    button_create_dir = tk.Button(root, text="Save", command=lambda: f_create_dir(en11_file.get()))
    button_create_dir.pack(padx=10, pady=5)

    button_save_xls = tk.Button(root, text="Save Trajectory", state=tk.DISABLED, command=lambda: f_save_csv(coord_mat, time_vec, str(en11_file.get())))

    label_save_current_map = tk.Label(root, text="Save Current Map")
    en13_file = tk.Entry(root)
    en13_file.insert(0, 'figure_name')
    button_save_map = tk.Button(root, text="Save Current Map", state=tk.DISABLED, command=lambda: f_save_map(str(en11_file.get()), str(en13_file.get()), fig))

def enable_second_widgets():
    button_save_xls.config(state=tk.NORMAL)
    label_save_current_map.pack(padx=10, pady=5)
    en13_file.pack(padx=10, pady=5)
    button_save_map.config(state=tk.NORMAL)
    button_save_map.pack(padx=10, pady=5)
    button_save_xls.pack(padx=10, pady=5)

root.mainloop()