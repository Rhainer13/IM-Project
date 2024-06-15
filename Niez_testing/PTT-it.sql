PGDMP      9                |            PTT-IT Test    16.2    16.2 7    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    25098    PTT-IT Test    DATABASE     �   CREATE DATABASE "PTT-IT Test" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_United States.1252';
    DROP DATABASE "PTT-IT Test";
                postgres    false            �            1255    25185    fnc_insert_history_receipt()    FUNCTION     �   CREATE FUNCTION public.fnc_insert_history_receipt() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
	INSERT INTO HISTORY(HISTORY_ID, RECEIPT_ID)
	VALUES(DEFAULT, NEW.RECEIPT_ID);
END
$$;
 3   DROP FUNCTION public.fnc_insert_history_receipt();
       public          postgres    false            �            1255    25183    fnc_insert_history_service()    FUNCTION     �   CREATE FUNCTION public.fnc_insert_history_service() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
	INSERT INTO HISTORY(HISTORY_ID, SERVICE_ID)
	VALUES(DEFAULT, NEW.SERVICE_ID);
RETURN NEW;
END
$$;
 3   DROP FUNCTION public.fnc_insert_history_service();
       public          postgres    false            �            1259    25132    employee    TABLE     L  CREATE TABLE public.employee (
    employee_id integer NOT NULL,
    employee_lname character varying(25) NOT NULL,
    employee_fname character varying(25) NOT NULL,
    employee_address character varying(100) NOT NULL,
    employee_cont_no character varying(11) NOT NULL,
    employee_date_hired date DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.employee;
       public         heap    postgres    false            �            1259    25131    employee_employee_id_seq    SEQUENCE     �   CREATE SEQUENCE public.employee_employee_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.employee_employee_id_seq;
       public          postgres    false    222            �           0    0    employee_employee_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.employee_employee_id_seq OWNED BY public.employee.employee_id;
          public          postgres    false    221            �            1259    25166    history    TABLE     q   CREATE TABLE public.history (
    history_id integer NOT NULL,
    receipt_id integer,
    service_id integer
);
    DROP TABLE public.history;
       public         heap    postgres    false            �            1259    25165    history_history_id_seq    SEQUENCE     �   CREATE SEQUENCE public.history_history_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.history_history_id_seq;
       public          postgres    false    226            �           0    0    history_history_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.history_history_id_seq OWNED BY public.history.history_id;
          public          postgres    false    225            �            1259    25115 
   order_item    TABLE     �   CREATE TABLE public.order_item (
    order_item_id integer NOT NULL,
    order_qty integer NOT NULL,
    order_price numeric(9,2) NOT NULL,
    receipt_id integer NOT NULL,
    product_id integer NOT NULL
);
    DROP TABLE public.order_item;
       public         heap    postgres    false            �            1259    25114    order_item_order_item_id_seq    SEQUENCE     �   CREATE SEQUENCE public.order_item_order_item_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.order_item_order_item_id_seq;
       public          postgres    false    220            �           0    0    order_item_order_item_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.order_item_order_item_id_seq OWNED BY public.order_item.order_item_id;
          public          postgres    false    219            �            1259    25100    products    TABLE     �   CREATE TABLE public.products (
    product_id integer NOT NULL,
    product_name character varying(50) NOT NULL,
    product_qty integer NOT NULL,
    prod_category character varying(25) NOT NULL,
    product_price numeric(9,2) NOT NULL
);
    DROP TABLE public.products;
       public         heap    postgres    false            �            1259    25099    products_product_id_seq    SEQUENCE     �   CREATE SEQUENCE public.products_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.products_product_id_seq;
       public          postgres    false    216            �           0    0    products_product_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.products_product_id_seq OWNED BY public.products.product_id;
          public          postgres    false    215            �            1259    25107    receipt    TABLE     �   CREATE TABLE public.receipt (
    receipt_id integer NOT NULL,
    receipt_cus_name character varying(50) NOT NULL,
    receipt_total numeric(9,2) NOT NULL,
    receipt_date date DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.receipt;
       public         heap    postgres    false            �            1259    25106    receipt_receipt_id_seq    SEQUENCE     �   CREATE SEQUENCE public.receipt_receipt_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.receipt_receipt_id_seq;
       public          postgres    false    218            �           0    0    receipt_receipt_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.receipt_receipt_id_seq OWNED BY public.receipt.receipt_id;
          public          postgres    false    217            �            1259    25153    service    TABLE     W  CREATE TABLE public.service (
    service_id integer NOT NULL,
    service_cus_name character varying(25) NOT NULL,
    service_device character varying(25) NOT NULL,
    service_type character varying(50) NOT NULL,
    service_charge numeric(9,2) NOT NULL,
    employee_id integer NOT NULL,
    service_date date DEFAULT CURRENT_TIMESTAMP
);
    DROP TABLE public.service;
       public         heap    postgres    false            �            1259    25152    service_service_id_seq    SEQUENCE     �   CREATE SEQUENCE public.service_service_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.service_service_id_seq;
       public          postgres    false    224            �           0    0    service_service_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.service_service_id_seq OWNED BY public.service.service_id;
          public          postgres    false    223            9           2604    25135    employee employee_id    DEFAULT     |   ALTER TABLE ONLY public.employee ALTER COLUMN employee_id SET DEFAULT nextval('public.employee_employee_id_seq'::regclass);
 C   ALTER TABLE public.employee ALTER COLUMN employee_id DROP DEFAULT;
       public          postgres    false    221    222    222            =           2604    25169    history history_id    DEFAULT     x   ALTER TABLE ONLY public.history ALTER COLUMN history_id SET DEFAULT nextval('public.history_history_id_seq'::regclass);
 A   ALTER TABLE public.history ALTER COLUMN history_id DROP DEFAULT;
       public          postgres    false    225    226    226            8           2604    25118    order_item order_item_id    DEFAULT     �   ALTER TABLE ONLY public.order_item ALTER COLUMN order_item_id SET DEFAULT nextval('public.order_item_order_item_id_seq'::regclass);
 G   ALTER TABLE public.order_item ALTER COLUMN order_item_id DROP DEFAULT;
       public          postgres    false    219    220    220            5           2604    25103    products product_id    DEFAULT     z   ALTER TABLE ONLY public.products ALTER COLUMN product_id SET DEFAULT nextval('public.products_product_id_seq'::regclass);
 B   ALTER TABLE public.products ALTER COLUMN product_id DROP DEFAULT;
       public          postgres    false    216    215    216            6           2604    25110    receipt receipt_id    DEFAULT     x   ALTER TABLE ONLY public.receipt ALTER COLUMN receipt_id SET DEFAULT nextval('public.receipt_receipt_id_seq'::regclass);
 A   ALTER TABLE public.receipt ALTER COLUMN receipt_id DROP DEFAULT;
       public          postgres    false    217    218    218            ;           2604    25156    service service_id    DEFAULT     x   ALTER TABLE ONLY public.service ALTER COLUMN service_id SET DEFAULT nextval('public.service_service_id_seq'::regclass);
 A   ALTER TABLE public.service ALTER COLUMN service_id DROP DEFAULT;
       public          postgres    false    223    224    224            �          0    25132    employee 
   TABLE DATA           �   COPY public.employee (employee_id, employee_lname, employee_fname, employee_address, employee_cont_no, employee_date_hired) FROM stdin;
    public          postgres    false    222   <C       �          0    25166    history 
   TABLE DATA           E   COPY public.history (history_id, receipt_id, service_id) FROM stdin;
    public          postgres    false    226   ~C       �          0    25115 
   order_item 
   TABLE DATA           c   COPY public.order_item (order_item_id, order_qty, order_price, receipt_id, product_id) FROM stdin;
    public          postgres    false    220   �C       �          0    25100    products 
   TABLE DATA           g   COPY public.products (product_id, product_name, product_qty, prod_category, product_price) FROM stdin;
    public          postgres    false    216   �C       �          0    25107    receipt 
   TABLE DATA           \   COPY public.receipt (receipt_id, receipt_cus_name, receipt_total, receipt_date) FROM stdin;
    public          postgres    false    218   �C       �          0    25153    service 
   TABLE DATA           �   COPY public.service (service_id, service_cus_name, service_device, service_type, service_charge, employee_id, service_date) FROM stdin;
    public          postgres    false    224   �C       �           0    0    employee_employee_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.employee_employee_id_seq', 3, true);
          public          postgres    false    221            �           0    0    history_history_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.history_history_id_seq', 6, true);
          public          postgres    false    225            �           0    0    order_item_order_item_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.order_item_order_item_id_seq', 2, true);
          public          postgres    false    219            �           0    0    products_product_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.products_product_id_seq', 1, true);
          public          postgres    false    215            �           0    0    receipt_receipt_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.receipt_receipt_id_seq', 2, true);
          public          postgres    false    217            �           0    0    service_service_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.service_service_id_seq', 6, true);
          public          postgres    false    223            E           2606    25138    employee employee_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (employee_id);
 @   ALTER TABLE ONLY public.employee DROP CONSTRAINT employee_pkey;
       public            postgres    false    222            I           2606    25171    history history_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.history
    ADD CONSTRAINT history_pkey PRIMARY KEY (history_id);
 >   ALTER TABLE ONLY public.history DROP CONSTRAINT history_pkey;
       public            postgres    false    226            C           2606    25120    order_item order_item_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.order_item
    ADD CONSTRAINT order_item_pkey PRIMARY KEY (order_item_id);
 D   ALTER TABLE ONLY public.order_item DROP CONSTRAINT order_item_pkey;
       public            postgres    false    220            ?           2606    25105    products products_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (product_id);
 @   ALTER TABLE ONLY public.products DROP CONSTRAINT products_pkey;
       public            postgres    false    216            A           2606    25113    receipt receipt_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.receipt
    ADD CONSTRAINT receipt_pkey PRIMARY KEY (receipt_id);
 >   ALTER TABLE ONLY public.receipt DROP CONSTRAINT receipt_pkey;
       public            postgres    false    218            G           2606    25159    service service_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.service
    ADD CONSTRAINT service_pkey PRIMARY KEY (service_id);
 >   ALTER TABLE ONLY public.service DROP CONSTRAINT service_pkey;
       public            postgres    false    224            O           2620    25186 "   receipt trg_insert_history_service    TRIGGER     �   CREATE TRIGGER trg_insert_history_service AFTER INSERT ON public.receipt FOR EACH ROW EXECUTE FUNCTION public.fnc_insert_history_receipt();
 ;   DROP TRIGGER trg_insert_history_service ON public.receipt;
       public          postgres    false    227    218            P           2620    25184 "   service trg_insert_history_service    TRIGGER     �   CREATE TRIGGER trg_insert_history_service AFTER INSERT ON public.service FOR EACH ROW EXECUTE FUNCTION public.fnc_insert_history_service();
 ;   DROP TRIGGER trg_insert_history_service ON public.service;
       public          postgres    false    228    224            M           2606    25172    history history_receipt_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.history
    ADD CONSTRAINT history_receipt_id_fkey FOREIGN KEY (receipt_id) REFERENCES public.receipt(receipt_id);
 I   ALTER TABLE ONLY public.history DROP CONSTRAINT history_receipt_id_fkey;
       public          postgres    false    226    4673    218            N           2606    25177    history history_service_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.history
    ADD CONSTRAINT history_service_id_fkey FOREIGN KEY (service_id) REFERENCES public.service(service_id);
 I   ALTER TABLE ONLY public.history DROP CONSTRAINT history_service_id_fkey;
       public          postgres    false    226    224    4679            J           2606    25126 %   order_item order_item_product_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.order_item
    ADD CONSTRAINT order_item_product_id_fkey FOREIGN KEY (product_id) REFERENCES public.products(product_id);
 O   ALTER TABLE ONLY public.order_item DROP CONSTRAINT order_item_product_id_fkey;
       public          postgres    false    4671    216    220            K           2606    25121 %   order_item order_item_receipt_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.order_item
    ADD CONSTRAINT order_item_receipt_id_fkey FOREIGN KEY (receipt_id) REFERENCES public.receipt(receipt_id);
 O   ALTER TABLE ONLY public.order_item DROP CONSTRAINT order_item_receipt_id_fkey;
       public          postgres    false    220    4673    218            L           2606    25160     service service_employee_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.service
    ADD CONSTRAINT service_employee_id_fkey FOREIGN KEY (employee_id) REFERENCES public.employee(employee_id);
 J   ALTER TABLE ONLY public.service DROP CONSTRAINT service_employee_id_fkey;
       public          postgres    false    224    4677    222            �   2   x�3�tru�������4426153��40�4202�50�50����� ���      �      x�3���4����� �      �      x������ � �      �      x������ � �      �      x������ � �      �   ;   x�3�t�Spuq���q��t�qu���s�450�30�4�4202�50�50����� &�
L     