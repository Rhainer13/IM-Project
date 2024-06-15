PGDMP  (    -                |            test_5    16.2    16.2 Z               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    21083    test_5    DATABASE        CREATE DATABASE test_5 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Philippines.1252';
    DROP DATABASE test_5;
                postgres    false            �            1255    21116    fnc_product_after_insert()    FUNCTION       CREATE FUNCTION public.fnc_product_after_insert() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
begin
-- 	inventory
	insert into inventory(prod_id)
	values (new.prod_id);
		
-- 	cpu
	if new.prod_cat ilike 'CPU' then
		insert into cpu(prod_id)
		values (new.prod_id);
	end if;
	
-- 	ram
	if new.prod_cat ilike 'RAM' then
		insert into ram(prod_id)
		values (new.prod_id);
	end if;
	
-- 	motherboard
	if new.prod_cat ilike 'Motherboard' then
		insert into motherboard(prod_id)
		values (new.prod_id);
	end if;
	
	return new;
end;
$$;
 1   DROP FUNCTION public.fnc_product_after_insert();
       public          postgres    false            �            1259    21203    cart    TABLE     x   CREATE TABLE public.cart (
    cart_id integer NOT NULL,
    cart_qty integer DEFAULT 1,
    inv_id integer NOT NULL
);
    DROP TABLE public.cart;
       public         heap    postgres    false            �            1259    21201    cart_cart_id_seq    SEQUENCE     �   CREATE SEQUENCE public.cart_cart_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.cart_cart_id_seq;
       public          postgres    false    228                       0    0    cart_cart_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.cart_cart_id_seq OWNED BY public.cart.cart_id;
          public          postgres    false    226            �            1259    21202    cart_inv_id_seq    SEQUENCE     �   CREATE SEQUENCE public.cart_inv_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.cart_inv_id_seq;
       public          postgres    false    228                       0    0    cart_inv_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.cart_inv_id_seq OWNED BY public.cart.inv_id;
          public          postgres    false    227            �            1259    21260    completed_orders    TABLE     �  CREATE TABLE public.completed_orders (
    comp_id integer NOT NULL,
    comp_date timestamp without time zone,
    comp_cust_name character varying(50),
    comp_prod_brand character varying(50),
    comp_prod_name character varying(50),
    comp_prod_cat character varying(50),
    comp_prod_price double precision,
    comp_qty integer,
    comp_total double precision,
    inv_id integer
);
 $   DROP TABLE public.completed_orders;
       public         heap    postgres    false            �            1259    21259    completed_orders_comp_id_seq    SEQUENCE     �   CREATE SEQUENCE public.completed_orders_comp_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.completed_orders_comp_id_seq;
       public          postgres    false    230                        0    0    completed_orders_comp_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.completed_orders_comp_id_seq OWNED BY public.completed_orders.comp_id;
          public          postgres    false    229            �            1259    21104    cpu    TABLE     V   CREATE TABLE public.cpu (
    prod_id integer NOT NULL,
    cpu_core_count integer
);
    DROP TABLE public.cpu;
       public         heap    postgres    false            �            1259    21103    cpu_prod_id_seq    SEQUENCE     �   CREATE SEQUENCE public.cpu_prod_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.cpu_prod_id_seq;
       public          postgres    false    218            !           0    0    cpu_prod_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.cpu_prod_id_seq OWNED BY public.cpu.prod_id;
          public          postgres    false    217            �            1259    21308    device    TABLE     `   CREATE TABLE public.device (
    dev_id integer NOT NULL,
    dev_type character varying(50)
);
    DROP TABLE public.device;
       public         heap    postgres    false            �            1259    21307    device_dev_id_seq    SEQUENCE     �   CREATE SEQUENCE public.device_dev_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.device_dev_id_seq;
       public          postgres    false    234            "           0    0    device_dev_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.device_dev_id_seq OWNED BY public.device.dev_id;
          public          postgres    false    233            �            1259    21149 	   inventory    TABLE     |   CREATE TABLE public.inventory (
    inv_id integer NOT NULL,
    inv_qty integer DEFAULT 0,
    prod_id integer NOT NULL
);
    DROP TABLE public.inventory;
       public         heap    postgres    false            �            1259    21147    inventory_inv_id_seq    SEQUENCE     �   CREATE SEQUENCE public.inventory_inv_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.inventory_inv_id_seq;
       public          postgres    false    221            #           0    0    inventory_inv_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.inventory_inv_id_seq OWNED BY public.inventory.inv_id;
          public          postgres    false    219            �            1259    21148    inventory_prod_id_seq    SEQUENCE     �   CREATE SEQUENCE public.inventory_prod_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.inventory_prod_id_seq;
       public          postgres    false    221            $           0    0    inventory_prod_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.inventory_prod_id_seq OWNED BY public.inventory.prod_id;
          public          postgres    false    220            �            1259    21175    motherboard    TABLE     e   CREATE TABLE public.motherboard (
    prod_id integer NOT NULL,
    mb_size character varying(50)
);
    DROP TABLE public.motherboard;
       public         heap    postgres    false            �            1259    21174    motherboard_prod_id_seq    SEQUENCE     �   CREATE SEQUENCE public.motherboard_prod_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.motherboard_prod_id_seq;
       public          postgres    false    225            %           0    0    motherboard_prod_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.motherboard_prod_id_seq OWNED BY public.motherboard.prod_id;
          public          postgres    false    224            �            1259    21085    product    TABLE     �   CREATE TABLE public.product (
    prod_id integer NOT NULL,
    prod_brand character varying(50),
    prod_name character varying(50),
    prod_price double precision,
    prod_cat character varying(50)
);
    DROP TABLE public.product;
       public         heap    postgres    false            �            1259    21084    product_prod_id_seq    SEQUENCE     �   CREATE SEQUENCE public.product_prod_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.product_prod_id_seq;
       public          postgres    false    216            &           0    0    product_prod_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.product_prod_id_seq OWNED BY public.product.prod_id;
          public          postgres    false    215            �            1259    21163    ram    TABLE     P   CREATE TABLE public.ram (
    prod_id integer NOT NULL,
    ram_size integer
);
    DROP TABLE public.ram;
       public         heap    postgres    false            �            1259    21162    ram_prod_id_seq    SEQUENCE     �   CREATE SEQUENCE public.ram_prod_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.ram_prod_id_seq;
       public          postgres    false    223            '           0    0    ram_prod_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.ram_prod_id_seq OWNED BY public.ram.prod_id;
          public          postgres    false    222            �            1259    21315    service    TABLE     c   CREATE TABLE public.service (
    serv_id integer NOT NULL,
    serv_type character varying(50)
);
    DROP TABLE public.service;
       public         heap    postgres    false            �            1259    21314    service_serv_id_seq    SEQUENCE     �   CREATE SEQUENCE public.service_serv_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.service_serv_id_seq;
       public          postgres    false    236            (           0    0    service_serv_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.service_serv_id_seq OWNED BY public.service.serv_id;
          public          postgres    false    235            �            1259    21301    staff    TABLE     �   CREATE TABLE public.staff (
    staff_id integer NOT NULL,
    staff_fname character varying(50),
    staff_lname character varying(50),
    staff_mob_num character(11),
    staff_addr character varying(50),
    staff_hire_date date
);
    DROP TABLE public.staff;
       public         heap    postgres    false            �            1259    21300    staff_staff_id_seq    SEQUENCE     �   CREATE SEQUENCE public.staff_staff_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.staff_staff_id_seq;
       public          postgres    false    232            )           0    0    staff_staff_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.staff_staff_id_seq OWNED BY public.staff.staff_id;
          public          postgres    false    231            Q           2604    21206    cart cart_id    DEFAULT     l   ALTER TABLE ONLY public.cart ALTER COLUMN cart_id SET DEFAULT nextval('public.cart_cart_id_seq'::regclass);
 ;   ALTER TABLE public.cart ALTER COLUMN cart_id DROP DEFAULT;
       public          postgres    false    228    226    228            S           2604    21208    cart inv_id    DEFAULT     j   ALTER TABLE ONLY public.cart ALTER COLUMN inv_id SET DEFAULT nextval('public.cart_inv_id_seq'::regclass);
 :   ALTER TABLE public.cart ALTER COLUMN inv_id DROP DEFAULT;
       public          postgres    false    227    228    228            T           2604    21263    completed_orders comp_id    DEFAULT     �   ALTER TABLE ONLY public.completed_orders ALTER COLUMN comp_id SET DEFAULT nextval('public.completed_orders_comp_id_seq'::regclass);
 G   ALTER TABLE public.completed_orders ALTER COLUMN comp_id DROP DEFAULT;
       public          postgres    false    229    230    230            K           2604    21107    cpu prod_id    DEFAULT     j   ALTER TABLE ONLY public.cpu ALTER COLUMN prod_id SET DEFAULT nextval('public.cpu_prod_id_seq'::regclass);
 :   ALTER TABLE public.cpu ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    217    218    218            V           2604    21311    device dev_id    DEFAULT     n   ALTER TABLE ONLY public.device ALTER COLUMN dev_id SET DEFAULT nextval('public.device_dev_id_seq'::regclass);
 <   ALTER TABLE public.device ALTER COLUMN dev_id DROP DEFAULT;
       public          postgres    false    234    233    234            L           2604    21152    inventory inv_id    DEFAULT     t   ALTER TABLE ONLY public.inventory ALTER COLUMN inv_id SET DEFAULT nextval('public.inventory_inv_id_seq'::regclass);
 ?   ALTER TABLE public.inventory ALTER COLUMN inv_id DROP DEFAULT;
       public          postgres    false    219    221    221            N           2604    21154    inventory prod_id    DEFAULT     v   ALTER TABLE ONLY public.inventory ALTER COLUMN prod_id SET DEFAULT nextval('public.inventory_prod_id_seq'::regclass);
 @   ALTER TABLE public.inventory ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    220    221    221            P           2604    21178    motherboard prod_id    DEFAULT     z   ALTER TABLE ONLY public.motherboard ALTER COLUMN prod_id SET DEFAULT nextval('public.motherboard_prod_id_seq'::regclass);
 B   ALTER TABLE public.motherboard ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    225    224    225            J           2604    21088    product prod_id    DEFAULT     r   ALTER TABLE ONLY public.product ALTER COLUMN prod_id SET DEFAULT nextval('public.product_prod_id_seq'::regclass);
 >   ALTER TABLE public.product ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    215    216    216            O           2604    21166    ram prod_id    DEFAULT     j   ALTER TABLE ONLY public.ram ALTER COLUMN prod_id SET DEFAULT nextval('public.ram_prod_id_seq'::regclass);
 :   ALTER TABLE public.ram ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    222    223    223            W           2604    21318    service serv_id    DEFAULT     r   ALTER TABLE ONLY public.service ALTER COLUMN serv_id SET DEFAULT nextval('public.service_serv_id_seq'::regclass);
 >   ALTER TABLE public.service ALTER COLUMN serv_id DROP DEFAULT;
       public          postgres    false    235    236    236            U           2604    21304    staff staff_id    DEFAULT     p   ALTER TABLE ONLY public.staff ALTER COLUMN staff_id SET DEFAULT nextval('public.staff_staff_id_seq'::regclass);
 =   ALTER TABLE public.staff ALTER COLUMN staff_id DROP DEFAULT;
       public          postgres    false    232    231    232                      0    21203    cart 
   TABLE DATA           9   COPY public.cart (cart_id, cart_qty, inv_id) FROM stdin;
    public          postgres    false    228   f                 0    21260    completed_orders 
   TABLE DATA           �   COPY public.completed_orders (comp_id, comp_date, comp_cust_name, comp_prod_brand, comp_prod_name, comp_prod_cat, comp_prod_price, comp_qty, comp_total, inv_id) FROM stdin;
    public          postgres    false    230   3f                 0    21104    cpu 
   TABLE DATA           6   COPY public.cpu (prod_id, cpu_core_count) FROM stdin;
    public          postgres    false    218   Pf                 0    21308    device 
   TABLE DATA           2   COPY public.device (dev_id, dev_type) FROM stdin;
    public          postgres    false    234   mf                 0    21149 	   inventory 
   TABLE DATA           =   COPY public.inventory (inv_id, inv_qty, prod_id) FROM stdin;
    public          postgres    false    221   �f                 0    21175    motherboard 
   TABLE DATA           7   COPY public.motherboard (prod_id, mb_size) FROM stdin;
    public          postgres    false    225   �f                 0    21085    product 
   TABLE DATA           W   COPY public.product (prod_id, prod_brand, prod_name, prod_price, prod_cat) FROM stdin;
    public          postgres    false    216   �f       
          0    21163    ram 
   TABLE DATA           0   COPY public.ram (prod_id, ram_size) FROM stdin;
    public          postgres    false    223   �f                 0    21315    service 
   TABLE DATA           5   COPY public.service (serv_id, serv_type) FROM stdin;
    public          postgres    false    236   g                 0    21301    staff 
   TABLE DATA           o   COPY public.staff (staff_id, staff_fname, staff_lname, staff_mob_num, staff_addr, staff_hire_date) FROM stdin;
    public          postgres    false    232   Mg       *           0    0    cart_cart_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.cart_cart_id_seq', 126, true);
          public          postgres    false    226            +           0    0    cart_inv_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.cart_inv_id_seq', 1, false);
          public          postgres    false    227            ,           0    0    completed_orders_comp_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.completed_orders_comp_id_seq', 10, true);
          public          postgres    false    229            -           0    0    cpu_prod_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.cpu_prod_id_seq', 1, false);
          public          postgres    false    217            .           0    0    device_dev_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.device_dev_id_seq', 2, true);
          public          postgres    false    233            /           0    0    inventory_inv_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.inventory_inv_id_seq', 34, true);
          public          postgres    false    219            0           0    0    inventory_prod_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.inventory_prod_id_seq', 1, false);
          public          postgres    false    220            1           0    0    motherboard_prod_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.motherboard_prod_id_seq', 1, false);
          public          postgres    false    224            2           0    0    product_prod_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.product_prod_id_seq', 41, true);
          public          postgres    false    215            3           0    0    ram_prod_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.ram_prod_id_seq', 1, false);
          public          postgres    false    222            4           0    0    service_serv_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.service_serv_id_seq', 3, true);
          public          postgres    false    235            5           0    0    staff_staff_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.staff_staff_id_seq', 6, true);
          public          postgres    false    231            c           2606    21210    cart cart_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.cart
    ADD CONSTRAINT cart_pkey PRIMARY KEY (cart_id);
 8   ALTER TABLE ONLY public.cart DROP CONSTRAINT cart_pkey;
       public            postgres    false    228            e           2606    21265 &   completed_orders completed_orders_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.completed_orders
    ADD CONSTRAINT completed_orders_pkey PRIMARY KEY (comp_id);
 P   ALTER TABLE ONLY public.completed_orders DROP CONSTRAINT completed_orders_pkey;
       public            postgres    false    230            [           2606    21109    cpu cpu_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY public.cpu
    ADD CONSTRAINT cpu_pkey PRIMARY KEY (prod_id);
 6   ALTER TABLE ONLY public.cpu DROP CONSTRAINT cpu_pkey;
       public            postgres    false    218            i           2606    21313    device device_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.device
    ADD CONSTRAINT device_pkey PRIMARY KEY (dev_id);
 <   ALTER TABLE ONLY public.device DROP CONSTRAINT device_pkey;
       public            postgres    false    234            ]           2606    21156    inventory inventory_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.inventory
    ADD CONSTRAINT inventory_pkey PRIMARY KEY (inv_id);
 B   ALTER TABLE ONLY public.inventory DROP CONSTRAINT inventory_pkey;
       public            postgres    false    221            a           2606    21180    motherboard motherboard_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.motherboard
    ADD CONSTRAINT motherboard_pkey PRIMARY KEY (prod_id);
 F   ALTER TABLE ONLY public.motherboard DROP CONSTRAINT motherboard_pkey;
       public            postgres    false    225            Y           2606    21090    product product_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (prod_id);
 >   ALTER TABLE ONLY public.product DROP CONSTRAINT product_pkey;
       public            postgres    false    216            _           2606    21168    ram ram_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY public.ram
    ADD CONSTRAINT ram_pkey PRIMARY KEY (prod_id);
 6   ALTER TABLE ONLY public.ram DROP CONSTRAINT ram_pkey;
       public            postgres    false    223            k           2606    21320    service service_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.service
    ADD CONSTRAINT service_pkey PRIMARY KEY (serv_id);
 >   ALTER TABLE ONLY public.service DROP CONSTRAINT service_pkey;
       public            postgres    false    236            g           2606    21306    staff staff_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.staff
    ADD CONSTRAINT staff_pkey PRIMARY KEY (staff_id);
 :   ALTER TABLE ONLY public.staff DROP CONSTRAINT staff_pkey;
       public            postgres    false    232            r           2620    21117     product trg_product_after_insert    TRIGGER     �   CREATE TRIGGER trg_product_after_insert AFTER INSERT ON public.product FOR EACH ROW EXECUTE FUNCTION public.fnc_product_after_insert();
 9   DROP TRIGGER trg_product_after_insert ON public.product;
       public          postgres    false    216    237            p           2606    21211    cart cart_inv_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.cart
    ADD CONSTRAINT cart_inv_id_fkey FOREIGN KEY (inv_id) REFERENCES public.inventory(inv_id) ON UPDATE CASCADE ON DELETE CASCADE;
 ?   ALTER TABLE ONLY public.cart DROP CONSTRAINT cart_inv_id_fkey;
       public          postgres    false    221    228    4701            q           2606    21266 -   completed_orders completed_orders_inv_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.completed_orders
    ADD CONSTRAINT completed_orders_inv_id_fkey FOREIGN KEY (inv_id) REFERENCES public.inventory(inv_id) ON DELETE SET NULL;
 W   ALTER TABLE ONLY public.completed_orders DROP CONSTRAINT completed_orders_inv_id_fkey;
       public          postgres    false    4701    230    221            l           2606    21110    cpu cpu_prod_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.cpu
    ADD CONSTRAINT cpu_prod_id_fkey FOREIGN KEY (prod_id) REFERENCES public.product(prod_id) ON UPDATE CASCADE ON DELETE CASCADE;
 >   ALTER TABLE ONLY public.cpu DROP CONSTRAINT cpu_prod_id_fkey;
       public          postgres    false    4697    216    218            m           2606    21157     inventory inventory_prod_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.inventory
    ADD CONSTRAINT inventory_prod_id_fkey FOREIGN KEY (prod_id) REFERENCES public.product(prod_id) ON UPDATE CASCADE ON DELETE CASCADE;
 J   ALTER TABLE ONLY public.inventory DROP CONSTRAINT inventory_prod_id_fkey;
       public          postgres    false    4697    216    221            o           2606    21181 $   motherboard motherboard_prod_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.motherboard
    ADD CONSTRAINT motherboard_prod_id_fkey FOREIGN KEY (prod_id) REFERENCES public.product(prod_id) ON UPDATE CASCADE ON DELETE CASCADE;
 N   ALTER TABLE ONLY public.motherboard DROP CONSTRAINT motherboard_prod_id_fkey;
       public          postgres    false    225    216    4697            n           2606    21169    ram ram_prod_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.ram
    ADD CONSTRAINT ram_prod_id_fkey FOREIGN KEY (prod_id) REFERENCES public.product(prod_id) ON UPDATE CASCADE ON DELETE CASCADE;
 >   ALTER TABLE ONLY public.ram DROP CONSTRAINT ram_prod_id_fkey;
       public          postgres    false    216    223    4697                  x������ � �            x������ � �            x������ � �         !   x�3�tI-�.�/Pp�2��I, ��b���� m�/            x������ � �            x������ � �            x������ � �      
      x������ � �         +   x�3�t�IM���K�2�J-H�,�2�-H/JLI����� �P	�         D   x�M�+�@ Q=����l������5���w�F�q��઺���I:�x7���"�
��(V��"���     