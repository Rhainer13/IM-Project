PGDMP               	        |         
   ptt_sample    16.2    16.2     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    19699 
   ptt_sample    DATABASE     �   CREATE DATABASE ptt_sample WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Philippines.1252';
    DROP DATABASE ptt_sample;
                postgres    false            �            1259    19720    employee    TABLE       CREATE TABLE public.employee (
    emp_id integer NOT NULL,
    emp_name character varying(50) NOT NULL,
    emp_date_hired date NOT NULL,
    emp_addr character varying(50) NOT NULL,
    emp_cont character varying(11) NOT NULL,
    emp_charge numeric(5,2) NOT NULL
);
    DROP TABLE public.employee;
       public         heap    postgres    false            �            1259    19719    employee_emp_id_seq    SEQUENCE     �   CREATE SEQUENCE public.employee_emp_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.employee_emp_id_seq;
       public          postgres    false    216            �           0    0    employee_emp_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.employee_emp_id_seq OWNED BY public.employee.emp_id;
          public          postgres    false    215            �            1259    19727 	   inventory    TABLE     �   CREATE TABLE public.inventory (
    prod_id integer NOT NULL,
    prod_name character varying(50) NOT NULL,
    prod_qty smallint NOT NULL,
    prod_price smallint NOT NULL,
    prod_cat character varying(50) NOT NULL
);
    DROP TABLE public.inventory;
       public         heap    postgres    false            �            1259    19726    inventory_prod_id_seq    SEQUENCE     �   CREATE SEQUENCE public.inventory_prod_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.inventory_prod_id_seq;
       public          postgres    false    218            �           0    0    inventory_prod_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.inventory_prod_id_seq OWNED BY public.inventory.prod_id;
          public          postgres    false    217            �            1259    19734    test    TABLE     �   CREATE TABLE public.test (
    test_id integer NOT NULL,
    test_attr1 character varying(50),
    test_attr2 character varying(50)
);
    DROP TABLE public.test;
       public         heap    postgres    false            �            1259    19733    test_test_id_seq    SEQUENCE     �   CREATE SEQUENCE public.test_test_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.test_test_id_seq;
       public          postgres    false    220            �           0    0    test_test_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.test_test_id_seq OWNED BY public.test.test_id;
          public          postgres    false    219            $           2604    19723    employee emp_id    DEFAULT     r   ALTER TABLE ONLY public.employee ALTER COLUMN emp_id SET DEFAULT nextval('public.employee_emp_id_seq'::regclass);
 >   ALTER TABLE public.employee ALTER COLUMN emp_id DROP DEFAULT;
       public          postgres    false    216    215    216            %           2604    19730    inventory prod_id    DEFAULT     v   ALTER TABLE ONLY public.inventory ALTER COLUMN prod_id SET DEFAULT nextval('public.inventory_prod_id_seq'::regclass);
 @   ALTER TABLE public.inventory ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    218    217    218            &           2604    19737    test test_id    DEFAULT     l   ALTER TABLE ONLY public.test ALTER COLUMN test_id SET DEFAULT nextval('public.test_test_id_seq'::regclass);
 ;   ALTER TABLE public.test ALTER COLUMN test_id DROP DEFAULT;
       public          postgres    false    220    219    220            �          0    19720    employee 
   TABLE DATA           d   COPY public.employee (emp_id, emp_name, emp_date_hired, emp_addr, emp_cont, emp_charge) FROM stdin;
    public          postgres    false    216   �       �          0    19727 	   inventory 
   TABLE DATA           W   COPY public.inventory (prod_id, prod_name, prod_qty, prod_price, prod_cat) FROM stdin;
    public          postgres    false    218   _       �          0    19734    test 
   TABLE DATA           ?   COPY public.test (test_id, test_attr1, test_attr2) FROM stdin;
    public          postgres    false    220   �       �           0    0    employee_emp_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.employee_emp_id_seq', 10, true);
          public          postgres    false    215            �           0    0    inventory_prod_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.inventory_prod_id_seq', 16, true);
          public          postgres    false    217            �           0    0    test_test_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.test_test_id_seq', 24, true);
          public          postgres    false    219            (           2606    19725    employee employee_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.employee
    ADD CONSTRAINT employee_pkey PRIMARY KEY (emp_id);
 @   ALTER TABLE ONLY public.employee DROP CONSTRAINT employee_pkey;
       public            postgres    false    216            *           2606    19732    inventory inventory_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.inventory
    ADD CONSTRAINT inventory_pkey PRIMARY KEY (prod_id);
 B   ALTER TABLE ONLY public.inventory DROP CONSTRAINT inventory_pkey;
       public            postgres    false    218            ,           2606    19739    test test_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.test
    ADD CONSTRAINT test_pkey PRIMARY KEY (test_id);
 8   ALTER TABLE ONLY public.test DROP CONSTRAINT test_pkey;
       public            postgres    false    220            �   �   x�}�;
1E��yـI�{I��������p]=1����!$��fjx���� J@6`�A	P.�����`{(,5@�@��h? 4X:�v�[����060`9`
171a��)�/?C�      �      x�3�,(�OQ0�A����Ԣ��Ģ.��':�rBD�4�䗧)8'�rA�8!(�ї˔����?D���S�ߓ��� ��-14���L��2� ����9�\F��h j9�E1z\\\ �3Z      �   B   x�3�L�LN�24�L�LL�24���22�B dv�n)#cNC#c 224�L,N�!� ������ ��$     