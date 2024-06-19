PGDMP  7    7                |            ptt    16.2    16.2 �    N           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            O           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            P           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            Q           1262    21734    ptt    DATABASE     |   CREATE DATABASE ptt WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Philippines.1252';
    DROP DATABASE ptt;
                postgres    false            �            1255    21959 #   fnc_completed_orders_after_insert()    FUNCTION     �   CREATE FUNCTION public.fnc_completed_orders_after_insert() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
	INSERT INTO
		SALES_RECORD(SALES_REC_TYPE, COMP_ID)
	VALUES
		('PURCHASE', NEW.COMP_ID);
	RETURN NEW;
END;
$$;
 :   DROP FUNCTION public.fnc_completed_orders_after_insert();
       public          postgres    false            �            1255    21908    fnc_product_after_insert()    FUNCTION       CREATE FUNCTION public.fnc_product_after_insert() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
-- 	INVENTORY
	INSERT INTO INVENTORY(PROD_ID)
	VALUES (NEW.PROD_ID);
		
-- 	CPU
	IF NEW.PROD_CAT ILIKE 'CPU' THEN
		INSERT INTO CPU(PROD_ID)
		VALUES (NEW.PROD_ID);
	END IF;
	
-- 	RAM
	IF NEW.PROD_CAT ILIKE 'RAM' THEN
		INSERT INTO RAM(PROD_ID)
		VALUES (NEW.PROD_ID);
	END IF;
	
-- 	MOTHERBOARD
	IF NEW.PROD_CAT ILIKE 'MOTHERBOARD' THEN
		INSERT INTO MOTHERBOARD(PROD_ID)
		VALUES (NEW.PROD_ID);
	END IF;
	
-- 	STORAGE DRIVE
	IF NEW.PROD_CAT ILIKE 'STORAGE DRIVE' THEN
		INSERT INTO STORAGE_DRIVE(PROD_ID)
		VALUES (NEW.PROD_ID);
	END IF;
	
-- 	STORAGE DRIVE
	IF NEW.PROD_CAT ILIKE 'PSU' THEN
		INSERT INTO PSU(PROD_ID)
		VALUES (NEW.PROD_ID);
	END IF;
	
	RETURN NEW;
END;
$$;
 1   DROP FUNCTION public.fnc_product_after_insert();
       public          postgres    false            �            1255    21961 "   fnc_service_details_after_insert()    FUNCTION     �   CREATE FUNCTION public.fnc_service_details_after_insert() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
	INSERT INTO
		SALES_RECORD(SALES_REC_TYPE, SERV_DET_ID)
	VALUES
		('SERVICE', NEW.SERV_DET_ID);
	RETURN NEW;
END;
$$;
 9   DROP FUNCTION public.fnc_service_details_after_insert();
       public          postgres    false            �            1259    21821    cart    TABLE     �   CREATE TABLE public.cart (
    cart_id integer NOT NULL,
    cart_qty integer DEFAULT 1 NOT NULL,
    inv_id integer NOT NULL
);
    DROP TABLE public.cart;
       public         heap    postgres    false            �            1259    21819    cart_cart_id_seq    SEQUENCE     �   CREATE SEQUENCE public.cart_cart_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.cart_cart_id_seq;
       public          postgres    false    222            R           0    0    cart_cart_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.cart_cart_id_seq OWNED BY public.cart.cart_id;
          public          postgres    false    220            �            1259    21820    cart_inv_id_seq    SEQUENCE     �   CREATE SEQUENCE public.cart_inv_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.cart_inv_id_seq;
       public          postgres    false    222            S           0    0    cart_inv_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.cart_inv_id_seq OWNED BY public.cart.inv_id;
          public          postgres    false    221            �            1259    21835    completed_orders    TABLE     �  CREATE TABLE public.completed_orders (
    comp_id integer NOT NULL,
    comp_date timestamp without time zone NOT NULL,
    comp_cust_name character varying(50) NOT NULL,
    comp_prod_brand character varying(50) NOT NULL,
    comp_prod_name character varying(50) NOT NULL,
    comp_prod_cat character varying(50) NOT NULL,
    comp_prod_price double precision NOT NULL,
    comp_qty integer NOT NULL,
    comp_total double precision NOT NULL,
    inv_id integer
);
 $   DROP TABLE public.completed_orders;
       public         heap    postgres    false            �            1259    21834    completed_orders_comp_id_seq    SEQUENCE     �   CREATE SEQUENCE public.completed_orders_comp_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.completed_orders_comp_id_seq;
       public          postgres    false    224            T           0    0    completed_orders_comp_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.completed_orders_comp_id_seq OWNED BY public.completed_orders.comp_id;
          public          postgres    false    223            �            1259    21911    cpu    TABLE     V   CREATE TABLE public.cpu (
    prod_id integer NOT NULL,
    cpu_core_count integer
);
    DROP TABLE public.cpu;
       public         heap    postgres    false            �            1259    21910    cpu_prod_id_seq    SEQUENCE     �   CREATE SEQUENCE public.cpu_prod_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.cpu_prod_id_seq;
       public          postgres    false    236            U           0    0    cpu_prod_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.cpu_prod_id_seq OWNED BY public.cpu.prod_id;
          public          postgres    false    235            �            1259    21855    device    TABLE     i   CREATE TABLE public.device (
    dev_id integer NOT NULL,
    dev_type character varying(50) NOT NULL
);
    DROP TABLE public.device;
       public         heap    postgres    false            �            1259    21854    device_dev_id_seq    SEQUENCE     �   CREATE SEQUENCE public.device_dev_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.device_dev_id_seq;
       public          postgres    false    228            V           0    0    device_dev_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.device_dev_id_seq OWNED BY public.device.dev_id;
          public          postgres    false    227            �            1259    21806 	   inventory    TABLE     �   CREATE TABLE public.inventory (
    inv_id integer NOT NULL,
    inv_qty integer DEFAULT 0 NOT NULL,
    prod_id integer NOT NULL
);
    DROP TABLE public.inventory;
       public         heap    postgres    false            �            1259    21804    inventory_inv_id_seq    SEQUENCE     �   CREATE SEQUENCE public.inventory_inv_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.inventory_inv_id_seq;
       public          postgres    false    219            W           0    0    inventory_inv_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.inventory_inv_id_seq OWNED BY public.inventory.inv_id;
          public          postgres    false    217            �            1259    21805    inventory_prod_id_seq    SEQUENCE     �   CREATE SEQUENCE public.inventory_prod_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.inventory_prod_id_seq;
       public          postgres    false    219            X           0    0    inventory_prod_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.inventory_prod_id_seq OWNED BY public.inventory.prod_id;
          public          postgres    false    218            �            1259    21936    motherboard    TABLE     e   CREATE TABLE public.motherboard (
    prod_id integer NOT NULL,
    mb_size character varying(50)
);
    DROP TABLE public.motherboard;
       public         heap    postgres    false            �            1259    21935    motherboard_prod_id_seq    SEQUENCE     �   CREATE SEQUENCE public.motherboard_prod_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.motherboard_prod_id_seq;
       public          postgres    false    240            Y           0    0    motherboard_prod_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.motherboard_prod_id_seq OWNED BY public.motherboard.prod_id;
          public          postgres    false    239            �            1259    21736    product    TABLE     �   CREATE TABLE public.product (
    prod_id integer NOT NULL,
    prod_brand character varying(50) NOT NULL,
    prod_name character varying(50) NOT NULL,
    prod_price double precision NOT NULL,
    prod_cat character varying(50) NOT NULL
);
    DROP TABLE public.product;
       public         heap    postgres    false            �            1259    21735    product_prod_id_seq    SEQUENCE     �   CREATE SEQUENCE public.product_prod_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.product_prod_id_seq;
       public          postgres    false    216            Z           0    0    product_prod_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.product_prod_id_seq OWNED BY public.product.prod_id;
          public          postgres    false    215            �            1259    21977    psu    TABLE     Q   CREATE TABLE public.psu (
    prod_id integer NOT NULL,
    psu_watts integer
);
    DROP TABLE public.psu;
       public         heap    postgres    false            �            1259    21976    psu_prod_id_seq    SEQUENCE     �   CREATE SEQUENCE public.psu_prod_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.psu_prod_id_seq;
       public          postgres    false    244            [           0    0    psu_prod_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.psu_prod_id_seq OWNED BY public.psu.prod_id;
          public          postgres    false    243            �            1259    21924    ram    TABLE     P   CREATE TABLE public.ram (
    prod_id integer NOT NULL,
    ram_size integer
);
    DROP TABLE public.ram;
       public         heap    postgres    false            �            1259    21923    ram_prod_id_seq    SEQUENCE     �   CREATE SEQUENCE public.ram_prod_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.ram_prod_id_seq;
       public          postgres    false    238            \           0    0    ram_prod_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.ram_prod_id_seq OWNED BY public.ram.prod_id;
          public          postgres    false    237            �            1259    21892    sales_record    TABLE     �   CREATE TABLE public.sales_record (
    sales_rec_id integer NOT NULL,
    sales_rec_type character varying(50) NOT NULL,
    serv_det_id integer,
    comp_id integer
);
     DROP TABLE public.sales_record;
       public         heap    postgres    false            �            1259    21891    sales_record_sales_rec_id_seq    SEQUENCE     �   CREATE SEQUENCE public.sales_record_sales_rec_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.sales_record_sales_rec_id_seq;
       public          postgres    false    234            ]           0    0    sales_record_sales_rec_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.sales_record_sales_rec_id_seq OWNED BY public.sales_record.sales_rec_id;
          public          postgres    false    233            �            1259    21862    service    TABLE     l   CREATE TABLE public.service (
    serv_id integer NOT NULL,
    serv_type character varying(50) NOT NULL
);
    DROP TABLE public.service;
       public         heap    postgres    false            �            1259    21869    service_details    TABLE     �  CREATE TABLE public.service_details (
    serv_det_id integer NOT NULL,
    serv_det_date timestamp without time zone NOT NULL,
    serv_det_cust_name character varying(50) NOT NULL,
    serv_det_total_fee double precision NOT NULL,
    serv_det_stat character varying(50) DEFAULT 'ONGOING'::character varying NOT NULL,
    staff_id integer,
    dev_id integer,
    serv_id integer
);
 #   DROP TABLE public.service_details;
       public         heap    postgres    false            �            1259    21868    service_details_serv_det_id_seq    SEQUENCE     �   CREATE SEQUENCE public.service_details_serv_det_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 6   DROP SEQUENCE public.service_details_serv_det_id_seq;
       public          postgres    false    232            ^           0    0    service_details_serv_det_id_seq    SEQUENCE OWNED BY     c   ALTER SEQUENCE public.service_details_serv_det_id_seq OWNED BY public.service_details.serv_det_id;
          public          postgres    false    231            �            1259    21861    service_serv_id_seq    SEQUENCE     �   CREATE SEQUENCE public.service_serv_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.service_serv_id_seq;
       public          postgres    false    230            _           0    0    service_serv_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.service_serv_id_seq OWNED BY public.service.serv_id;
          public          postgres    false    229            �            1259    21848    staff    TABLE       CREATE TABLE public.staff (
    staff_id integer NOT NULL,
    staff_fname character varying(50) NOT NULL,
    staff_lname character varying(50) NOT NULL,
    staff_mob_num character(11) NOT NULL,
    staff_addr character varying(50) NOT NULL,
    staff_hire_date date NOT NULL
);
    DROP TABLE public.staff;
       public         heap    postgres    false            �            1259    21847    staff_staff_id_seq    SEQUENCE     �   CREATE SEQUENCE public.staff_staff_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.staff_staff_id_seq;
       public          postgres    false    226            `           0    0    staff_staff_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.staff_staff_id_seq OWNED BY public.staff.staff_id;
          public          postgres    false    225            �            1259    21948    storage_drive    TABLE     |   CREATE TABLE public.storage_drive (
    prod_id integer NOT NULL,
    sd_size integer,
    sd_type character varying(50)
);
 !   DROP TABLE public.storage_drive;
       public         heap    postgres    false            �            1259    21947    storage_drive_prod_id_seq    SEQUENCE     �   CREATE SEQUENCE public.storage_drive_prod_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.storage_drive_prod_id_seq;
       public          postgres    false    242            a           0    0    storage_drive_prod_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.storage_drive_prod_id_seq OWNED BY public.storage_drive.prod_id;
          public          postgres    false    241            d           2604    21824    cart cart_id    DEFAULT     l   ALTER TABLE ONLY public.cart ALTER COLUMN cart_id SET DEFAULT nextval('public.cart_cart_id_seq'::regclass);
 ;   ALTER TABLE public.cart ALTER COLUMN cart_id DROP DEFAULT;
       public          postgres    false    222    220    222            f           2604    21826    cart inv_id    DEFAULT     j   ALTER TABLE ONLY public.cart ALTER COLUMN inv_id SET DEFAULT nextval('public.cart_inv_id_seq'::regclass);
 :   ALTER TABLE public.cart ALTER COLUMN inv_id DROP DEFAULT;
       public          postgres    false    222    221    222            g           2604    21838    completed_orders comp_id    DEFAULT     �   ALTER TABLE ONLY public.completed_orders ALTER COLUMN comp_id SET DEFAULT nextval('public.completed_orders_comp_id_seq'::regclass);
 G   ALTER TABLE public.completed_orders ALTER COLUMN comp_id DROP DEFAULT;
       public          postgres    false    224    223    224            n           2604    21914    cpu prod_id    DEFAULT     j   ALTER TABLE ONLY public.cpu ALTER COLUMN prod_id SET DEFAULT nextval('public.cpu_prod_id_seq'::regclass);
 :   ALTER TABLE public.cpu ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    236    235    236            i           2604    21858    device dev_id    DEFAULT     n   ALTER TABLE ONLY public.device ALTER COLUMN dev_id SET DEFAULT nextval('public.device_dev_id_seq'::regclass);
 <   ALTER TABLE public.device ALTER COLUMN dev_id DROP DEFAULT;
       public          postgres    false    227    228    228            a           2604    21809    inventory inv_id    DEFAULT     t   ALTER TABLE ONLY public.inventory ALTER COLUMN inv_id SET DEFAULT nextval('public.inventory_inv_id_seq'::regclass);
 ?   ALTER TABLE public.inventory ALTER COLUMN inv_id DROP DEFAULT;
       public          postgres    false    217    219    219            c           2604    21811    inventory prod_id    DEFAULT     v   ALTER TABLE ONLY public.inventory ALTER COLUMN prod_id SET DEFAULT nextval('public.inventory_prod_id_seq'::regclass);
 @   ALTER TABLE public.inventory ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    218    219    219            p           2604    21939    motherboard prod_id    DEFAULT     z   ALTER TABLE ONLY public.motherboard ALTER COLUMN prod_id SET DEFAULT nextval('public.motherboard_prod_id_seq'::regclass);
 B   ALTER TABLE public.motherboard ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    240    239    240            `           2604    21739    product prod_id    DEFAULT     r   ALTER TABLE ONLY public.product ALTER COLUMN prod_id SET DEFAULT nextval('public.product_prod_id_seq'::regclass);
 >   ALTER TABLE public.product ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    215    216    216            r           2604    21980    psu prod_id    DEFAULT     j   ALTER TABLE ONLY public.psu ALTER COLUMN prod_id SET DEFAULT nextval('public.psu_prod_id_seq'::regclass);
 :   ALTER TABLE public.psu ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    244    243    244            o           2604    21927    ram prod_id    DEFAULT     j   ALTER TABLE ONLY public.ram ALTER COLUMN prod_id SET DEFAULT nextval('public.ram_prod_id_seq'::regclass);
 :   ALTER TABLE public.ram ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    238    237    238            m           2604    21895    sales_record sales_rec_id    DEFAULT     �   ALTER TABLE ONLY public.sales_record ALTER COLUMN sales_rec_id SET DEFAULT nextval('public.sales_record_sales_rec_id_seq'::regclass);
 H   ALTER TABLE public.sales_record ALTER COLUMN sales_rec_id DROP DEFAULT;
       public          postgres    false    234    233    234            j           2604    21865    service serv_id    DEFAULT     r   ALTER TABLE ONLY public.service ALTER COLUMN serv_id SET DEFAULT nextval('public.service_serv_id_seq'::regclass);
 >   ALTER TABLE public.service ALTER COLUMN serv_id DROP DEFAULT;
       public          postgres    false    230    229    230            k           2604    21872    service_details serv_det_id    DEFAULT     �   ALTER TABLE ONLY public.service_details ALTER COLUMN serv_det_id SET DEFAULT nextval('public.service_details_serv_det_id_seq'::regclass);
 J   ALTER TABLE public.service_details ALTER COLUMN serv_det_id DROP DEFAULT;
       public          postgres    false    232    231    232            h           2604    21851    staff staff_id    DEFAULT     p   ALTER TABLE ONLY public.staff ALTER COLUMN staff_id SET DEFAULT nextval('public.staff_staff_id_seq'::regclass);
 =   ALTER TABLE public.staff ALTER COLUMN staff_id DROP DEFAULT;
       public          postgres    false    225    226    226            q           2604    21951    storage_drive prod_id    DEFAULT     ~   ALTER TABLE ONLY public.storage_drive ALTER COLUMN prod_id SET DEFAULT nextval('public.storage_drive_prod_id_seq'::regclass);
 D   ALTER TABLE public.storage_drive ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    242    241    242            5          0    21821    cart 
   TABLE DATA           9   COPY public.cart (cart_id, cart_qty, inv_id) FROM stdin;
    public          postgres    false    222   ˛       7          0    21835    completed_orders 
   TABLE DATA           �   COPY public.completed_orders (comp_id, comp_date, comp_cust_name, comp_prod_brand, comp_prod_name, comp_prod_cat, comp_prod_price, comp_qty, comp_total, inv_id) FROM stdin;
    public          postgres    false    224   �       C          0    21911    cpu 
   TABLE DATA           6   COPY public.cpu (prod_id, cpu_core_count) FROM stdin;
    public          postgres    false    236   �       ;          0    21855    device 
   TABLE DATA           2   COPY public.device (dev_id, dev_type) FROM stdin;
    public          postgres    false    228   <�       2          0    21806 	   inventory 
   TABLE DATA           =   COPY public.inventory (inv_id, inv_qty, prod_id) FROM stdin;
    public          postgres    false    219   m�       G          0    21936    motherboard 
   TABLE DATA           7   COPY public.motherboard (prod_id, mb_size) FROM stdin;
    public          postgres    false    240   ĝ       /          0    21736    product 
   TABLE DATA           W   COPY public.product (prod_id, prod_brand, prod_name, prod_price, prod_cat) FROM stdin;
    public          postgres    false    216   �       K          0    21977    psu 
   TABLE DATA           1   COPY public.psu (prod_id, psu_watts) FROM stdin;
    public          postgres    false    244   3�       E          0    21924    ram 
   TABLE DATA           0   COPY public.ram (prod_id, ram_size) FROM stdin;
    public          postgres    false    238   \�       A          0    21892    sales_record 
   TABLE DATA           Z   COPY public.sales_record (sales_rec_id, sales_rec_type, serv_det_id, comp_id) FROM stdin;
    public          postgres    false    234   ��       =          0    21862    service 
   TABLE DATA           5   COPY public.service (serv_id, serv_type) FROM stdin;
    public          postgres    false    230   �       ?          0    21869    service_details 
   TABLE DATA           �   COPY public.service_details (serv_det_id, serv_det_date, serv_det_cust_name, serv_det_total_fee, serv_det_stat, staff_id, dev_id, serv_id) FROM stdin;
    public          postgres    false    232   *�       9          0    21848    staff 
   TABLE DATA           o   COPY public.staff (staff_id, staff_fname, staff_lname, staff_mob_num, staff_addr, staff_hire_date) FROM stdin;
    public          postgres    false    226           I          0    21948    storage_drive 
   TABLE DATA           B   COPY public.storage_drive (prod_id, sd_size, sd_type) FROM stdin;
    public          postgres    false    242   A�       b           0    0    cart_cart_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.cart_cart_id_seq', 70, true);
          public          postgres    false    220            c           0    0    cart_inv_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.cart_inv_id_seq', 1, false);
          public          postgres    false    221            d           0    0    completed_orders_comp_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.completed_orders_comp_id_seq', 11, true);
          public          postgres    false    223            e           0    0    cpu_prod_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.cpu_prod_id_seq', 1, false);
          public          postgres    false    235            f           0    0    device_dev_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.device_dev_id_seq', 5, true);
          public          postgres    false    227            g           0    0    inventory_inv_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.inventory_inv_id_seq', 37, true);
          public          postgres    false    217            h           0    0    inventory_prod_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.inventory_prod_id_seq', 1, false);
          public          postgres    false    218            i           0    0    motherboard_prod_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.motherboard_prod_id_seq', 1, false);
          public          postgres    false    239            j           0    0    product_prod_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.product_prod_id_seq', 37, true);
          public          postgres    false    215            k           0    0    psu_prod_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.psu_prod_id_seq', 1, false);
          public          postgres    false    243            l           0    0    ram_prod_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.ram_prod_id_seq', 1, false);
          public          postgres    false    237            m           0    0    sales_record_sales_rec_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.sales_record_sales_rec_id_seq', 13, true);
          public          postgres    false    233            n           0    0    service_details_serv_det_id_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.service_details_serv_det_id_seq', 7, true);
          public          postgres    false    231            o           0    0    service_serv_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.service_serv_id_seq', 3, true);
          public          postgres    false    229            p           0    0    staff_staff_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.staff_staff_id_seq', 7, true);
          public          postgres    false    225            q           0    0    storage_drive_prod_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.storage_drive_prod_id_seq', 1, false);
          public          postgres    false    241            x           2606    21828    cart cart_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.cart
    ADD CONSTRAINT cart_pkey PRIMARY KEY (cart_id);
 8   ALTER TABLE ONLY public.cart DROP CONSTRAINT cart_pkey;
       public            postgres    false    222            z           2606    21840 &   completed_orders completed_orders_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.completed_orders
    ADD CONSTRAINT completed_orders_pkey PRIMARY KEY (comp_id);
 P   ALTER TABLE ONLY public.completed_orders DROP CONSTRAINT completed_orders_pkey;
       public            postgres    false    224            �           2606    21916    cpu cpu_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY public.cpu
    ADD CONSTRAINT cpu_pkey PRIMARY KEY (prod_id);
 6   ALTER TABLE ONLY public.cpu DROP CONSTRAINT cpu_pkey;
       public            postgres    false    236            ~           2606    21860    device device_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.device
    ADD CONSTRAINT device_pkey PRIMARY KEY (dev_id);
 <   ALTER TABLE ONLY public.device DROP CONSTRAINT device_pkey;
       public            postgres    false    228            v           2606    21813    inventory inventory_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.inventory
    ADD CONSTRAINT inventory_pkey PRIMARY KEY (inv_id);
 B   ALTER TABLE ONLY public.inventory DROP CONSTRAINT inventory_pkey;
       public            postgres    false    219            �           2606    21941    motherboard motherboard_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.motherboard
    ADD CONSTRAINT motherboard_pkey PRIMARY KEY (prod_id);
 F   ALTER TABLE ONLY public.motherboard DROP CONSTRAINT motherboard_pkey;
       public            postgres    false    240            t           2606    21741    product product_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (prod_id);
 >   ALTER TABLE ONLY public.product DROP CONSTRAINT product_pkey;
       public            postgres    false    216            �           2606    21982    psu psu_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY public.psu
    ADD CONSTRAINT psu_pkey PRIMARY KEY (prod_id);
 6   ALTER TABLE ONLY public.psu DROP CONSTRAINT psu_pkey;
       public            postgres    false    244            �           2606    21929    ram ram_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY public.ram
    ADD CONSTRAINT ram_pkey PRIMARY KEY (prod_id);
 6   ALTER TABLE ONLY public.ram DROP CONSTRAINT ram_pkey;
       public            postgres    false    238            �           2606    21897    sales_record sales_record_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.sales_record
    ADD CONSTRAINT sales_record_pkey PRIMARY KEY (sales_rec_id);
 H   ALTER TABLE ONLY public.sales_record DROP CONSTRAINT sales_record_pkey;
       public            postgres    false    234            �           2606    21875 $   service_details service_details_pkey 
   CONSTRAINT     k   ALTER TABLE ONLY public.service_details
    ADD CONSTRAINT service_details_pkey PRIMARY KEY (serv_det_id);
 N   ALTER TABLE ONLY public.service_details DROP CONSTRAINT service_details_pkey;
       public            postgres    false    232            �           2606    21867    service service_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.service
    ADD CONSTRAINT service_pkey PRIMARY KEY (serv_id);
 >   ALTER TABLE ONLY public.service DROP CONSTRAINT service_pkey;
       public            postgres    false    230            |           2606    21853    staff staff_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.staff
    ADD CONSTRAINT staff_pkey PRIMARY KEY (staff_id);
 :   ALTER TABLE ONLY public.staff DROP CONSTRAINT staff_pkey;
       public            postgres    false    226            �           2606    21953     storage_drive storage_drive_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.storage_drive
    ADD CONSTRAINT storage_drive_pkey PRIMARY KEY (prod_id);
 J   ALTER TABLE ONLY public.storage_drive DROP CONSTRAINT storage_drive_pkey;
       public            postgres    false    242            �           2620    21960 2   completed_orders trg_completed_orders_after_insert    TRIGGER     �   CREATE TRIGGER trg_completed_orders_after_insert AFTER INSERT ON public.completed_orders FOR EACH ROW EXECUTE FUNCTION public.fnc_completed_orders_after_insert();
 K   DROP TRIGGER trg_completed_orders_after_insert ON public.completed_orders;
       public          postgres    false    245    224            �           2620    21909     product trg_product_after_insert    TRIGGER     �   CREATE TRIGGER trg_product_after_insert AFTER INSERT ON public.product FOR EACH ROW EXECUTE FUNCTION public.fnc_product_after_insert();
 9   DROP TRIGGER trg_product_after_insert ON public.product;
       public          postgres    false    216    247            �           2620    21962 0   service_details trg_service_details_after_insert    TRIGGER     �   CREATE TRIGGER trg_service_details_after_insert AFTER INSERT ON public.service_details FOR EACH ROW EXECUTE FUNCTION public.fnc_service_details_after_insert();
 I   DROP TRIGGER trg_service_details_after_insert ON public.service_details;
       public          postgres    false    232    246            �           2606    21829    cart cart_inv_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.cart
    ADD CONSTRAINT cart_inv_id_fkey FOREIGN KEY (inv_id) REFERENCES public.inventory(inv_id) ON UPDATE CASCADE ON DELETE CASCADE;
 ?   ALTER TABLE ONLY public.cart DROP CONSTRAINT cart_inv_id_fkey;
       public          postgres    false    4726    222    219            �           2606    21841 -   completed_orders completed_orders_inv_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.completed_orders
    ADD CONSTRAINT completed_orders_inv_id_fkey FOREIGN KEY (inv_id) REFERENCES public.inventory(inv_id) ON DELETE SET NULL;
 W   ALTER TABLE ONLY public.completed_orders DROP CONSTRAINT completed_orders_inv_id_fkey;
       public          postgres    false    224    4726    219            �           2606    21917    cpu cpu_prod_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.cpu
    ADD CONSTRAINT cpu_prod_id_fkey FOREIGN KEY (prod_id) REFERENCES public.product(prod_id) ON UPDATE CASCADE ON DELETE CASCADE;
 >   ALTER TABLE ONLY public.cpu DROP CONSTRAINT cpu_prod_id_fkey;
       public          postgres    false    216    4724    236            �           2606    21814     inventory inventory_prod_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.inventory
    ADD CONSTRAINT inventory_prod_id_fkey FOREIGN KEY (prod_id) REFERENCES public.product(prod_id) ON UPDATE CASCADE ON DELETE CASCADE;
 J   ALTER TABLE ONLY public.inventory DROP CONSTRAINT inventory_prod_id_fkey;
       public          postgres    false    219    4724    216            �           2606    21942 $   motherboard motherboard_prod_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.motherboard
    ADD CONSTRAINT motherboard_prod_id_fkey FOREIGN KEY (prod_id) REFERENCES public.product(prod_id) ON UPDATE CASCADE ON DELETE CASCADE;
 N   ALTER TABLE ONLY public.motherboard DROP CONSTRAINT motherboard_prod_id_fkey;
       public          postgres    false    216    4724    240            �           2606    21983    psu psu_prod_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.psu
    ADD CONSTRAINT psu_prod_id_fkey FOREIGN KEY (prod_id) REFERENCES public.product(prod_id) ON UPDATE CASCADE ON DELETE CASCADE;
 >   ALTER TABLE ONLY public.psu DROP CONSTRAINT psu_prod_id_fkey;
       public          postgres    false    216    244    4724            �           2606    21930    ram ram_prod_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.ram
    ADD CONSTRAINT ram_prod_id_fkey FOREIGN KEY (prod_id) REFERENCES public.product(prod_id) ON UPDATE CASCADE ON DELETE CASCADE;
 >   ALTER TABLE ONLY public.ram DROP CONSTRAINT ram_prod_id_fkey;
       public          postgres    false    238    216    4724            �           2606    21903 &   sales_record sales_record_comp_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.sales_record
    ADD CONSTRAINT sales_record_comp_id_fkey FOREIGN KEY (comp_id) REFERENCES public.completed_orders(comp_id) ON UPDATE CASCADE ON DELETE CASCADE;
 P   ALTER TABLE ONLY public.sales_record DROP CONSTRAINT sales_record_comp_id_fkey;
       public          postgres    false    234    4730    224            �           2606    21898 *   sales_record sales_record_serv_det_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.sales_record
    ADD CONSTRAINT sales_record_serv_det_id_fkey FOREIGN KEY (serv_det_id) REFERENCES public.service_details(serv_det_id) ON UPDATE CASCADE ON DELETE CASCADE;
 T   ALTER TABLE ONLY public.sales_record DROP CONSTRAINT sales_record_serv_det_id_fkey;
       public          postgres    false    234    232    4738            �           2606    21881 +   service_details service_details_dev_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.service_details
    ADD CONSTRAINT service_details_dev_id_fkey FOREIGN KEY (dev_id) REFERENCES public.device(dev_id) ON UPDATE CASCADE ON DELETE CASCADE;
 U   ALTER TABLE ONLY public.service_details DROP CONSTRAINT service_details_dev_id_fkey;
       public          postgres    false    232    228    4734            �           2606    21886 ,   service_details service_details_serv_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.service_details
    ADD CONSTRAINT service_details_serv_id_fkey FOREIGN KEY (serv_id) REFERENCES public.service(serv_id) ON UPDATE CASCADE ON DELETE CASCADE;
 V   ALTER TABLE ONLY public.service_details DROP CONSTRAINT service_details_serv_id_fkey;
       public          postgres    false    232    4736    230            �           2606    21876 -   service_details service_details_staff_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.service_details
    ADD CONSTRAINT service_details_staff_id_fkey FOREIGN KEY (staff_id) REFERENCES public.staff(staff_id) ON DELETE SET NULL;
 W   ALTER TABLE ONLY public.service_details DROP CONSTRAINT service_details_staff_id_fkey;
       public          postgres    false    4732    232    226            �           2606    21954 (   storage_drive storage_drive_prod_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.storage_drive
    ADD CONSTRAINT storage_drive_prod_id_fkey FOREIGN KEY (prod_id) REFERENCES public.product(prod_id) ON UPDATE CASCADE ON DELETE CASCADE;
 R   ALTER TABLE ONLY public.storage_drive DROP CONSTRAINT storage_drive_prod_id_fkey;
       public          postgres    false    4724    242    216            5      x������ � �      7     x���?OA��z�Slo�����Ai0G8�P�\̅PɁ~~�,��xR��)���`Ѻ	�	%M.eG&Y�%���_5A�~��[H��[�W˦��t��m���(�`��7*w���bF6đ��Bݵ�����t��Κ����b2)�"Sf�ɚ��/$�S�ǰcJ���ߦ��1�3�VD��`v������P����Z�aU7ӥ1�]��oh<��x���^l&A�$T��J�j��o١+��]Ie�H���+�nX��aNB����QJ� Wȫ<      C       x�34�4�24�4�24�44�24�1z\\\ 5��      ;   !   x�3�tI-�.�/Pp�2��I, ��b���� n5      2   G   x����0C�s�0'iKwa�9�>�I��;tGn�1�JTF�6c�iL��������:��\��>���      G      x�3��t��2�S1z\\\ %�|      /   8  x�e�KO�@��w~�]jL�y0<�S^���i�q�J*����_j5�>�=���8�4 ��W(Qڔ����� L@r�=$Όq��{��"Z�n=���VP.ϲ�����`��P���y�btHo� ܑ�*%̆xnޛ�t�ߩ��5�P'�AaO�Ÿ�`T�Ag1�������"��$Q���9~�ou��V�+a�&�4�qky�p��}c�� ��u*�=0u���Jk��qR��vծƠk>k�]0�G<��s(���ea���
벍NG�D��`�-p�!7��m���2�0��1��09�OsB�I�q`      K      x�36�05�26�4R1z\\\ ��      E      x�34��241z\\\ �      A   ^   x�U�;
�0D���b$��K	mD�r���4�)ϝQ�=G���=�N�A;�\w+���/��d�0�q�#����j($�R�Е���x '�/      =   +   x�3�t�IM���K�2�J-H�,�2�-H/JLI����� �P	�      ?   �   x�e�;�0��>E.k�d��@G�����_Y���<�H" ��f�	�"T��F����4aB���x��i�$���T� -�Q8H��yk���e�uW�����_}}�;�T�\��݆�U
��;/%���0j      9   o   x�E�A� @�u{
.��☸lb��3�?ǰA���M�|!��/���G�ۦR��@�f��<~@w�YԜ\wi7�sw4z��p�Cr5��$r��tF
/
�����"�      I   "   x�3��4400�v�2��4�=\\�b���� M��     