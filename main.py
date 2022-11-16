import tkinter as tk
from tkinter import ttk
from graph import G
from algorithmes import *

window = tk.Tk()




window.geometry("1100x600")  
window.title("WSGraph App")
window.resizable(width=False,height=False)
bg = tk.PhotoImage(file="kkkkkkk2.png")
my_label=tk.Label(window, image=bg)
my_label.place(x=0,y=0,relwidth=1,relheight=1)
graph_info_frame = tk.Frame(window, pady=200, padx=200)
Page1 = tk.Frame(window,bg='white')
Page2 = tk.Frame(window,bg='white')
Page3 = tk.Frame(window,bg='white')  
Page4 = tk.Frame(window,bg='white')

Plusdinfo = tk.Frame(window)
Entries = []
is_oriented_var = tk.BooleanVar(Page2)
is_cout_var= tk.BooleanVar(Page2)
algorithm_input_variable = tk.StringVar(Page4)
K_list = []


    # Show Graph Information
def Tracer_graph():
    my_graph = G(Entries=Entries, cout_exist=is_cout_var.get())
    if is_oriented_var.get():
        my_graph.Tracer_DiGraph()
    else:
        my_graph.Tracer_Graph()
def show_graph_infos():
    # Show Graph Information
    my_graph = G(Entries=Entries, cout_exist=is_cout_var.get())
    my_graph.create_edges()
    my_graph.create_nodes()
    my_graph.create_list_Ad()
    my_graph.create_M_incidence()
    is_simple = my_graph.is_simple()
    is_complete = my_graph.is_complete()
    is_related = my_graph.True_associee()
    is_euler = my_graph.is_eulerian()
    graph_info_frame = tk.Frame(window, pady=100, padx=10)
    graph_info_frame.pack()
    caracteristics = tk.Label(graph_info_frame,text='Les Caractéristiques de votre graphe: 'f' {is_simple} ,'f' {is_complete} ,'f' {is_related} et 'f' {is_euler}')
    caracteristics.pack()
def apply_algorithm():
    my_graph = G(Entries=Entries, cout_exist=is_cout_var.get())
    algorithm_name = algorithm_input_variable.get()
    k_list = []

    def draw_result_kruskal():
        final_shape = GEntries=k_list, cout_exist=is_cout_var.get()
        final_shape.Tracer_graph()

    def draw_result_prim():
        final_shape_prim = G(Entries=run_prime(), cout_exist=is_cout_var.get())
        final_shape_prim.Tracer_graph()

    def draw_result_dijkstra():
        final_shape_dijkstra = G(Entries=run_dijkstra(), cout_exist=is_cout_var.get())
        final_shape_dijkstra.Tracer_graph()

    if algorithm_name == 'Kruskal':
        graph_info_frame.destroy()
        kruskal_frame = tk.Frame(window)
        kruskal_frame.pack()
        k_list = [(Entry_element[0] + Entry_element[2], Entry_element[1]) for Entry_element in my_graph.kruskal()]
        kruskal_header = tk.Label(kruskal_frame, text=f'list of edges : {k_list}', font='Arial 15')
        kruskal_header.pack()
        kruskal_draw_button = tk.Button(kruskal_frame, text="See also", command=draw_result_kruskal)
        kruskal_draw_button.pack()

    elif algorithm_name == 'Prime':

        def run_prime():
            prim_frame.destroy()
            prim2_frame = tk.Frame(window)
            prim2_frame.pack()
            prime_list = my_graph.prime(start_point.get())
            prim_header = tk.Label(prim2_frame, text=f'The list edges  : {prime_list}', font='Arial 15')
            prim_header.pack()
            prim_draw_button = tk.Button(prim2_frame, text="See also", command=draw_result_prim)
            prim_draw_button.pack()
            return prime_list

        graph_info_frame.destroy()
        prim_frame = tk.Frame(window)
        prim_frame.pack()
        prime_start_node_variable = tk.StringVar(prim_frame)
        prime_start_node_label = tk.Label(prim_frame, text="Starting point: ")
        prime_start_node_label.pack()
        prime_start_node_entry = tk.Entry(prim_frame, textvariable=prime_start_node_variable)
        prime_start_node_entry.pack()
        prime_start_node_button = tk.Button(prim_frame, text="Start", command=run_prime)
        prime_start_node_button.pack()
        start_point = prime_start_node_variable

    elif algorithm_name == 'Dijkstra':

        def run_dijkstra():
            dijkstra_frame.destroy()
            dijkstra2_frame = tk.Frame(window)
            dijkstra2_frame.pack()
            dijkstra_list = my_graph.dijkstra(start_point_dijkstra.get())
            dijkstra_header = tk.Label(dijkstra2_frame,
                                       text='final listes of your Graph : ',
                                       font='Arial 15')
            dijkstra_header.pack()
            dijkstra_table = tk.Label(dijkstra2_frame, text=f'{dijkstra_list}')
            dijkstra_table.pack()
            dijkstra_draw_button = tk.Button(dijkstra2_frame, text="See also", font='Arial 10' )  # command=draw_result_dijkstra
            dijkstra_draw_button.pack()

        graph_info_frame.destroy()
        dijkstra_frame = tk.Frame(window)
        dijkstra_frame.pack()
        dijkstra_start_node_variable = tk.StringVar(dijkstra_frame)
        dijkstra_start_node_label = tk.Label(dijkstra_frame, text="Starting point: ")
        dijkstra_start_node_label.pack()
        dijkstra_start_node_entry = tk.Entry(dijkstra_frame, textvariable=dijkstra_start_node_variable)
        dijkstra_start_node_entry.pack()
        dijkstra_start_node_button = tk.Button(dijkstra_frame, text="Start", command=run_dijkstra)
        dijkstra_start_node_button.pack()
        start_point_dijkstra = dijkstra_start_node_variable

    elif algorithm_name == 'Bellman-Ford':
        def run_bellmanf():
            bellmanf_frame.destroy()
            bellmanf2_frame = tk.Frame(window)
            bellmanf2_frame.pack()
            bellmanf_list = my_graph.bellman_ford(start_point_bellmanf.get())
            bellmanf_header = tk.Label(bellmanf2_frame,
                                       text=f'Finallist of your graph : ',
                                       font='Arial 15')
            bellmanf_header.pack()
            bellmanf_table = tk.Label(bellmanf2_frame, text=f'{bellmanf_list}')
            bellmanf_table.pack()
            bellmanf_draw_button = tk.Button(bellmanf2_frame, text="See also", )  # command=draw_result_dijkstra
            bellmanf_draw_button.pack()
            return bellmanf_list

        graph_info_frame.destroy()
        bellmanf_frame = tk.Frame(window)
        bellmanf_frame.pack()
        bellmanf_start_node_variable = tk.StringVar(bellmanf_frame)
        bellmanf_start_node_label = tk.Label(bellmanf_frame, text="Starting pointt: ")
        bellmanf_start_node_label.pack()
        bellmanf_start_node_entry = tk.Entry(bellmanf_frame, textvariable=bellmanf_start_node_variable)
        bellmanf_start_node_entry.pack()
        bellmanf_start_node_button = tk.Button(bellmanf_frame, text="Start", command=run_bellmanf)
        bellmanf_start_node_button.pack()
        start_point_bellmanf = bellmanf_start_node_variable

    elif algorithm_name == 'DFS':
        pass

    elif algorithm_name == 'BFS':
        pass




def PageFour():
    Page3.destroy()
    Page4 = tk.Frame(window,bg='white')
    Page4.pack(side="left" , padx = 10, pady = 10)
    main_label = tk.Label(Page4, text="Congratulations your graph is created", font="kefa 20",fg='red',bg='white')
    main_label.pack()
    Tracer_graph_label = tk.Label(Page4, text=" See your Graph :",bg='white', font="kefa 15")
    Tracer_graph_label.pack()
    Tracer_graph_button = tk.Button(Page4, text="See Graph", command=Tracer_graph)
    Tracer_graph_button.pack()
    Tracer_graph_info_label = tk.Label(Page4, text="See some informations about your graph :",bg='white', font="kefa 15")
    Tracer_graph_info_label.pack()
    Tracer_graph_info_button = tk.Button(Page4, text="See Now", command=show_graph_infos)
    Tracer_graph_info_button.pack()
   
    apply_algorithme_label = tk.Label(Page4, text="Would you like to know more features About \nyour graph so Choose your favorite algorithm ^^",bg='white', font="kefa 15")
    apply_algorithme_label.pack()
    values = ['Kruskal', 'Prime', 'Dijkstra', 'Bellman-Ford', 'BFS', 'DFS']
    algorithms_input = tk.OptionMenu(Page4, algorithm_input_variable, *values)
    algorithms_input.pack()
    algorithm_apply_button = tk.Button(Page4, text='Apply Now', command=apply_algorithm)
    algorithm_apply_button.pack()
    

def graph_info_page():
    
    Page1.destroy()
    Page2.pack(side="left" , padx = 110, pady = 10)
    

    lbl = tk.Label(Page2, text="Give the number of edges : ", font='Times 20 ', bg="white")
    lbl.pack()

    edges_variable = tk.IntVar(Page2)
    Tailleentry = tk.Entry(Page2, font='Courier 10 ', width=20, bg='lavender',textvariable=edges_variable)
    Tailleentry.pack()
    Tailleentry.focus_set()
    
    is_oriented_label = tk.Label(Page2, text="Give the type of graph:",font='Times 20 ', bg="white")
    is_oriented_label.pack()
    is_oriented_input = tk.Checkbutton(Page2, text="Oriented",variable=is_oriented_var, bg="white")
    is_oriented_input.pack()
    is_nonoriented_input = tk.Checkbutton(Page2, text="Non Oriented", bg="white")
    is_nonoriented_input.pack()
    

    is_cout_lbl = tk.Label(Page2, text="Would you like to be weighted ?", font='Times 20 ', bg="white")
    is_cout_lbl.pack()
    is_cout_entry = tk.Checkbutton(Page2,text="yes", variable=is_cout_var, bg="white")
    is_cout_entry.pack()
    is_cout_entry = tk.Checkbutton(Page2,text="no", bg="white")
    is_cout_entry.pack()
    edges_number_error = tk.Label(Page2, fg='red', bg="white")
    edges_number_error.pack()
    # The Third Page Where User Should Enter The Graph's edges infos
    def graph_edges_info_page():
        Page2.destroy()
        Page3.pack(side="left" , padx = 10, pady = 5)
        
        my_canvas = tk.Canvas(Page3,bg='white')
        my_canvas.pack(side="left", expand=1 ,padx=0,pady=0)

        scroll_bar = tk.Scrollbar(Page3, orient="vertical", command=my_canvas.yview)
        scroll_bar.pack(side="right", fill="y")

        my_canvas.configure(yscrollcommand=scroll_bar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

        Frame2 = tk.Frame(my_canvas,bg='white')
    
        my_canvas.create_window((600, 50), window=Frame2, anchor="nw")
        third_page_header = tk.Label(Frame2, text="fill the boxes below", font="kefa 15",bg='white')
        third_page_header.grid(row=0, columnspan=3)
        widgets_Entries_list = []

        # Get and Store The User Entries

        def append_Entries():
            for Entry_element in widgets_Entries_list:
                if is_cout_var.get():
                    Entries.append((Entry_element[0].get(), Entry_element[1].get()))
                else:
                    Entries.append(Entry_element.get())

            PageFour()

        # Get and Store The User Entries End

        # Generate The List Of Entries For User Entries(graph Information)

        edges_number = edges_variable.get()

        if is_cout_var.get():
            for i in range(edges_number):
                edge_weight_variable = tk.IntVar(Frame2)
                edge_name_label = tk.Label(Frame2, text=f'Edge : {i + 1}')
                edge_weight_label = tk.Label(Frame2, text=f'Cost : {i + 1}')
                edge_name_label.grid(row=i + 1, column=i - i)
                edge_weight_label.grid(row=i + 1, column=i + 2 - i)
                edge_name_entry = tk.Entry(Frame2 )
                edge_weight_entry = tk.Entry(Frame2, textvariable=edge_weight_variable)
                edge_name_entry.grid(row=i + 1, column=i - (i - 1))
                edge_weight_entry.grid(row=i + 1, column=i + 3 - (i - 1))
                edges_weight_error = tk.Label(Frame2, fg='pink')
                edges_weight_error.grid(row=i + 2, column=i + 3 - (i - 1))
                widgets_Entries_list.append((edge_name_entry, edge_weight_entry))

                # Error Handling
                def only_integer(data):
                    if data.isdigit():
                        return True
                    else:
                        return False

                def only_integers_errors(data):
                    edges_weight_error.configure(
                        text=f'Taper Un nombre Positive'
                    )

                register_only_ints = Page2.register(only_integer)
                register_only_errors = Page2.register(only_integers_errors)
                edge_weight_entry.config(validate='all',
                                         validatecommand=(register_only_ints, '%P'),
                                         invalidcommand=(register_only_errors, '%P'))
                # Error Handling End
        else:
            for i in range(edges_number):
                edge_name_label = tk.Label(Frame2, text=f'Arc {i}')
                edge_name_label.grid(row=i + 1, column=i - i )
                edge_name_entry = tk.Entry(Frame2, )
                edge_name_entry.grid(row=i + 1, column=i - (i - 1))
                widgets_Entries_list.append(edge_name_entry)

        # Generate The List Of Entries For User Entries(graph's Information) End

        # Submit Button for Entries
        show_Entries_button = tk.Button(Frame2, text="Creer le graphe", command=append_Entries,bg='#ADD8E6')
        show_Entries_button.grid(columnspan=2)
        label = tk.Label(Frame2, )
        label.grid()

        # Submit Button End

    # Start Error Handling for Edges Entry IN Page2

    def only_integers(data):
        if data.isdigit():
            return True
        else:
            return False

    def only_integers_error(data):
        edges_number_error.configure(
            text=f'Entrer Un Entier Positive'
        )

    register_only_int = Page2.register(only_integers)
    register_only_error = Page2.register(only_integers_error)
    Tailleentry.config(validate='all',
                       validatecommand=(register_only_int, '%P'),
                       invalidcommand=(register_only_error, '%P'))

    # End of Error Handling

    # Submit Button for Second page

    submit_button = tk.Button(Page2, text='Submit', command=graph_edges_info_page ,bg='#ADD8E6')
    submit_button.pack(padx=20, pady=10, ipady=5, ipadx=10)

    # Submit Button End

def Tracer_graph():
    my_graph = G(Entries=Entries, cout_exist=is_cout_var.get())
    if is_oriented_var.get():
        my_graph.Tracer_DiGraph()
    else:
        my_graph.Tracer_Graph()

def first_page():
    
    Plusdinfo.pack_forget()
    
    Page1.pack(side="left" , padx = 10, pady = 5)
     
    first_page_header = tk.Label(Page1, text="WSGraph Application provides you to \n Create graphs and apply a many algorithms\n ", bg='white',font='Kefa 18 ', fg='#5F9EA0')
    first_page_sub_header = tk.Label(Page1, text="Click in the button beLlow to begin", font='Kefa 18 ',bg='white', fg='black')
    first_page_header.pack()
    first_page_sub_header.pack()
    create_button = tk.Button(Page1, text="  Start ", bg='#ADD8E6',fg='#4169E1', font='Kefa 8 bold ',command=graph_info_page)
    create_button.pack(side='bottom',padx=20, pady=20, ipady=10, ipadx=15 )

def Plus_dinfo():
    
    Page1.pack_forget()
    Plusdinfo.pack()
    first_page_header = tk.Label(Plusdinfo, text="Ici vous allez trouver plus d'informations", font='Kefa 32 ', fg='#000')
    first_page_sub_header = tk.Label(Plusdinfo, text="C quoi la theori de graphe", font='Kefa 20 ', fg='#000')
    first_page_header.pack()
    first_page_sub_header.pack()
    create_button = tk.Button(Plusdinfo, text="  New graph ", bg='pink', command=graph_info_page)
    create_button.pack(padx=20, pady=10, ipady=5, ipadx=10)

#1) -creer la barre des menu

menuBar = tk.Menu(window,bg='gray')

# 2) -creer les menus principaux

buttonHome= tk.Button(menuBar)
buttonAbtus= tk.Button(menuBar)


# 3) -ajouter les menus principaux a la barre des menus
menuBar.add_cascade(label ="Home",menu=buttonHome,command=first_page , font =("Kefa",50))
menuBar.add_cascade(label ="Plus d'information",menu=buttonAbtus,command=Plus_dinfo, font =("Kefa",50))

window.config(menu=menuBar)


first_page()

window.mainloop()
