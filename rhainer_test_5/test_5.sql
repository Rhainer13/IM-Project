PGDMP                      |            test_5    16.2    16.2 1    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    21083    test_5    DATABASE        CREATE DATABASE test_5 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Philippines.1252';
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
       public          postgres    false            �            1259    21104    cpu    TABLE     V   CREATE TABLE public.cpu (
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
       public          postgres    false    218            �           0    0    cpu_prod_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.cpu_prod_id_seq OWNED BY public.cpu.prod_id;
          public          postgres    false    217            �            1259    21149 	   inventory    TABLE     |   CREATE TABLE public.inventory (
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
       public          postgres    false    221            �           0    0    inventory_inv_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.inventory_inv_id_seq OWNED BY public.inventory.inv_id;
          public          postgres    false    219            �            1259    21148    inventory_prod_id_seq    SEQUENCE     �   CREATE SEQUENCE public.inventory_prod_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.inventory_prod_id_seq;
       public          postgres    false    221            �           0    0    inventory_prod_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.inventory_prod_id_seq OWNED BY public.inventory.prod_id;
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
       public          postgres    false    225            �           0    0    motherboard_prod_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.motherboard_prod_id_seq OWNED BY public.motherboard.prod_id;
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
       public          postgres    false    216            �           0    0    product_prod_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.product_prod_id_seq OWNED BY public.product.prod_id;
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
       public          postgres    false    223            �           0    0    ram_prod_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.ram_prod_id_seq OWNED BY public.ram.prod_id;
          public          postgres    false    222            1           2604    21107    cpu prod_id    DEFAULT     j   ALTER TABLE ONLY public.cpu ALTER COLUMN prod_id SET DEFAULT nextval('public.cpu_prod_id_seq'::regclass);
 :   ALTER TABLE public.cpu ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    218    217    218            2           2604    21152    inventory inv_id    DEFAULT     t   ALTER TABLE ONLY public.inventory ALTER COLUMN inv_id SET DEFAULT nextval('public.inventory_inv_id_seq'::regclass);
 ?   ALTER TABLE public.inventory ALTER COLUMN inv_id DROP DEFAULT;
       public          postgres    false    219    221    221            4           2604    21154    inventory prod_id    DEFAULT     v   ALTER TABLE ONLY public.inventory ALTER COLUMN prod_id SET DEFAULT nextval('public.inventory_prod_id_seq'::regclass);
 @   ALTER TABLE public.inventory ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    220    221    221            6           2604    21178    motherboard prod_id    DEFAULT     z   ALTER TABLE ONLY public.motherboard ALTER COLUMN prod_id SET DEFAULT nextval('public.motherboard_prod_id_seq'::regclass);
 B   ALTER TABLE public.motherboard ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    225    224    225            0           2604    21088    product prod_id    DEFAULT     r   ALTER TABLE ONLY public.product ALTER COLUMN prod_id SET DEFAULT nextval('public.product_prod_id_seq'::regclass);
 >   ALTER TABLE public.product ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    216    215    216            5           2604    21166    ram prod_id    DEFAULT     j   ALTER TABLE ONLY public.ram ALTER COLUMN prod_id SET DEFAULT nextval('public.ram_prod_id_seq'::regclass);
 :   ALTER TABLE public.ram ALTER COLUMN prod_id DROP DEFAULT;
       public          postgres    false    222    223    223            �          0    21104    cpu 
   TABLE DATA           6   COPY public.cpu (prod_id, cpu_core_count) FROM stdin;
    public          postgres    false    218   Y7       �          0    21149 	   inventory 
   TABLE DATA           =   COPY public.inventory (inv_id, inv_qty, prod_id) FROM stdin;
    public          postgres    false    221   �7       �          0    21175    motherboard 
   TABLE DATA           7   COPY public.motherboard (prod_id, mb_size) FROM stdin;
    public          postgres    false    225   �7       �          0    21085    product 
   TABLE DATA           W   COPY public.product (prod_id, prod_brand, prod_name, prod_price, prod_cat) FROM stdin;
    public          postgres    false    216   �7       �          0    21163    ram 
   TABLE DATA           0   COPY public.ram (prod_id, ram_size) FROM stdin;
    public          postgres    false    223   �8       �           0    0    cpu_prod_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.cpu_prod_id_seq', 1, false);
          public          postgres    false    217            �           0    0    inventory_inv_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.inventory_inv_id_seq', 16, true);
          public          postgres    false    219            �           0    0    inventory_prod_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.inventory_prod_id_seq', 1, false);
          public          postgres    false    220            �           0    0    motherboard_prod_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.motherboard_prod_id_seq', 1, false);
          public          postgres    false    224            �           0    0    product_prod_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.product_prod_id_seq', 23, true);
          public          postgres    false    215            �           0    0    ram_prod_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.ram_prod_id_seq', 1, false);
          public          postgres    false    222            :           2606    21109    cpu cpu_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY public.cpu
    ADD CONSTRAINT cpu_pkey PRIMARY KEY (prod_id);
 6   ALTER TABLE ONLY public.cpu DROP CONSTRAINT cpu_pkey;
       public            postgres    false    218            <           2606    21156    inventory inventory_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.inventory
    ADD CONSTRAINT inventory_pkey PRIMARY KEY (inv_id);
 B   ALTER TABLE ONLY public.inventory DROP CONSTRAINT inventory_pkey;
       public            postgres    false    221            @           2606    21180    motherboard motherboard_pkey 
   CONSTRAINT     _   ALTER TABLE ONLY public.motherboard
    ADD CONSTRAINT motherboard_pkey PRIMARY KEY (prod_id);
 F   ALTER TABLE ONLY public.motherboard DROP CONSTRAINT motherboard_pkey;
       public            postgres    false    225            8           2606    21090    product product_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.product
    ADD CONSTRAINT product_pkey PRIMARY KEY (prod_id);
 >   ALTER TABLE ONLY public.product DROP CONSTRAINT product_pkey;
       public            postgres    false    216            >           2606    21168    ram ram_pkey 
   CONSTRAINT     O   ALTER TABLE ONLY public.ram
    ADD CONSTRAINT ram_pkey PRIMARY KEY (prod_id);
 6   ALTER TABLE ONLY public.ram DROP CONSTRAINT ram_pkey;
       public            postgres    false    223            E           2620    21117     product trg_product_after_insert    TRIGGER     �   CREATE TRIGGER trg_product_after_insert AFTER INSERT ON public.product FOR EACH ROW EXECUTE FUNCTION public.fnc_product_after_insert();
 9   DROP TRIGGER trg_product_after_insert ON public.product;
       public          postgres    false    216    226            A           2606    21110    cpu cpu_prod_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.cpu
    ADD CONSTRAINT cpu_prod_id_fkey FOREIGN KEY (prod_id) REFERENCES public.product(prod_id) ON UPDATE CASCADE ON DELETE CASCADE;
 >   ALTER TABLE ONLY public.cpu DROP CONSTRAINT cpu_prod_id_fkey;
       public          postgres    false    218    216    4664            B           2606    21157     inventory inventory_prod_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.inventory
    ADD CONSTRAINT inventory_prod_id_fkey FOREIGN KEY (prod_id) REFERENCES public.product(prod_id) ON UPDATE CASCADE ON DELETE CASCADE;
 J   ALTER TABLE ONLY public.inventory DROP CONSTRAINT inventory_prod_id_fkey;
       public          postgres    false    221    216    4664            D           2606    21181 $   motherboard motherboard_prod_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.motherboard
    ADD CONSTRAINT motherboard_prod_id_fkey FOREIGN KEY (prod_id) REFERENCES public.product(prod_id) ON UPDATE CASCADE ON DELETE CASCADE;
 N   ALTER TABLE ONLY public.motherboard DROP CONSTRAINT motherboard_prod_id_fkey;
       public          postgres    false    225    216    4664            C           2606    21169    ram ram_prod_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.ram
    ADD CONSTRAINT ram_prod_id_fkey FOREIGN KEY (prod_id) REFERENCES public.product(prod_id) ON UPDATE CASCADE ON DELETE CASCADE;
 >   ALTER TABLE ONLY public.ram DROP CONSTRAINT ram_prod_id_fkey;
       public          postgres    false    4664    223    216            �      x���4�bCNc.C# +F��� $��      �   :   x���� C�s~1>\�^���e-�h35�A���q����q��}�q�'|�7o	      �      x�32�t��22���L.��qb���� KT�      �   �   x�M���0����[��)M��K�$�����,������=������YA���t �J@CϠֿR�b1�m�(ـ+�0�d�fKjbr]��Yw01�����(��\���Ƚ㣍Mp�Nz��r���On+"� M2�      �      x�34�4�24�\1z\\\ X�     