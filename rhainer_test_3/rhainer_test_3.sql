PGDMP                      |            test_3    16.2    16.2 9    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    20785    test_3    DATABASE        CREATE DATABASE test_3 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'English_Philippines.1252';
    DROP DATABASE test_3;
                postgres    false            �            1255    20856    fnc_cpu_after_insert()    FUNCTION     �   CREATE FUNCTION public.fnc_cpu_after_insert() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
begin
	insert into
		inventory(cpu_id, inv_pc_part)
	values
		(new.cpu_id, 'CPU');
	return new;
end;
$$;
 -   DROP FUNCTION public.fnc_cpu_after_insert();
       public          postgres    false            �            1255    20860    fnc_mb_after_insert()    FUNCTION     �   CREATE FUNCTION public.fnc_mb_after_insert() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
begin
	insert into
		inventory(mb_id, inv_pc_part)
	values
		(new.mb_id, 'MOTHERBOARD');
	return new;
end;
$$;
 ,   DROP FUNCTION public.fnc_mb_after_insert();
       public          postgres    false            �            1255    20858    fnc_ram_after_insert()    FUNCTION     �   CREATE FUNCTION public.fnc_ram_after_insert() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
begin
	insert into
		inventory(ram_id, inv_pc_part)
	values
		(new.ram_id, 'RAM');
	return new;
end;
$$;
 -   DROP FUNCTION public.fnc_ram_after_insert();
       public          postgres    false            �            1259    20875    cart    TABLE     o   CREATE TABLE public.cart (
    cart_id integer NOT NULL,
    cart_qty integer DEFAULT 1,
    inv_id integer
);
    DROP TABLE public.cart;
       public         heap    postgres    false            �            1259    20874    cart_cart_id_seq    SEQUENCE     �   CREATE SEQUENCE public.cart_cart_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.cart_cart_id_seq;
       public          postgres    false    224            �           0    0    cart_cart_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.cart_cart_id_seq OWNED BY public.cart.cart_id;
          public          postgres    false    223            �            1259    20808    cpu    TABLE     �   CREATE TABLE public.cpu (
    cpu_id integer NOT NULL,
    name character varying(50),
    price double precision,
    core_count integer
);
    DROP TABLE public.cpu;
       public         heap    postgres    false            �            1259    20807    cpu_cpu_id_seq    SEQUENCE     �   CREATE SEQUENCE public.cpu_cpu_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.cpu_cpu_id_seq;
       public          postgres    false    216            �           0    0    cpu_cpu_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.cpu_cpu_id_seq OWNED BY public.cpu.cpu_id;
          public          postgres    false    215            �            1259    20829 	   inventory    TABLE     �   CREATE TABLE public.inventory (
    inv_id integer NOT NULL,
    inv_pc_part character varying(50),
    inv_qty integer,
    cpu_id integer,
    ram_id integer,
    mb_id integer
);
    DROP TABLE public.inventory;
       public         heap    postgres    false            �            1259    20828    inventory_inv_id_seq    SEQUENCE     �   CREATE SEQUENCE public.inventory_inv_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.inventory_inv_id_seq;
       public          postgres    false    222            �           0    0    inventory_inv_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.inventory_inv_id_seq OWNED BY public.inventory.inv_id;
          public          postgres    false    221            �            1259    20822    motherboard    TABLE     �   CREATE TABLE public.motherboard (
    mb_id integer NOT NULL,
    name character varying(50),
    price double precision,
    form_factor character varying(50)
);
    DROP TABLE public.motherboard;
       public         heap    postgres    false            �            1259    20821    motherboard_mb_id_seq    SEQUENCE     �   CREATE SEQUENCE public.motherboard_mb_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.motherboard_mb_id_seq;
       public          postgres    false    220            �           0    0    motherboard_mb_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.motherboard_mb_id_seq OWNED BY public.motherboard.mb_id;
          public          postgres    false    219            �            1259    21023    ordered_items    TABLE     >  CREATE TABLE public.ordered_items (
    ord_id integer NOT NULL,
    cart_id integer,
    ord_date timestamp without time zone,
    cust_name character varying(50),
    prod_name character varying(50),
    pc_part character varying(50),
    prod_price numeric(7,2),
    quantity integer,
    total double precision
);
 !   DROP TABLE public.ordered_items;
       public         heap    postgres    false            �            1259    21022    ordered_items_ord_id_seq    SEQUENCE     �   CREATE SEQUENCE public.ordered_items_ord_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.ordered_items_ord_id_seq;
       public          postgres    false    226            �           0    0    ordered_items_ord_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.ordered_items_ord_id_seq OWNED BY public.ordered_items.ord_id;
          public          postgres    false    225            �            1259    20815    ram    TABLE     �   CREATE TABLE public.ram (
    ram_id integer NOT NULL,
    name character varying(50),
    price double precision,
    size integer
);
    DROP TABLE public.ram;
       public         heap    postgres    false            �            1259    20814    ram_ram_id_seq    SEQUENCE     �   CREATE SEQUENCE public.ram_ram_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.ram_ram_id_seq;
       public          postgres    false    218            �           0    0    ram_ram_id_seq    SEQUENCE OWNED BY     A   ALTER SEQUENCE public.ram_ram_id_seq OWNED BY public.ram.ram_id;
          public          postgres    false    217            :           2604    20878    cart cart_id    DEFAULT     l   ALTER TABLE ONLY public.cart ALTER COLUMN cart_id SET DEFAULT nextval('public.cart_cart_id_seq'::regclass);
 ;   ALTER TABLE public.cart ALTER COLUMN cart_id DROP DEFAULT;
       public          postgres    false    224    223    224            6           2604    20811 
   cpu cpu_id    DEFAULT     h   ALTER TABLE ONLY public.cpu ALTER COLUMN cpu_id SET DEFAULT nextval('public.cpu_cpu_id_seq'::regclass);
 9   ALTER TABLE public.cpu ALTER COLUMN cpu_id DROP DEFAULT;
       public          postgres    false    216    215    216            9           2604    20832    inventory inv_id    DEFAULT     t   ALTER TABLE ONLY public.inventory ALTER COLUMN inv_id SET DEFAULT nextval('public.inventory_inv_id_seq'::regclass);
 ?   ALTER TABLE public.inventory ALTER COLUMN inv_id DROP DEFAULT;
       public          postgres    false    222    221    222            8           2604    20825    motherboard mb_id    DEFAULT     v   ALTER TABLE ONLY public.motherboard ALTER COLUMN mb_id SET DEFAULT nextval('public.motherboard_mb_id_seq'::regclass);
 @   ALTER TABLE public.motherboard ALTER COLUMN mb_id DROP DEFAULT;
       public          postgres    false    219    220    220            <           2604    21026    ordered_items ord_id    DEFAULT     |   ALTER TABLE ONLY public.ordered_items ALTER COLUMN ord_id SET DEFAULT nextval('public.ordered_items_ord_id_seq'::regclass);
 C   ALTER TABLE public.ordered_items ALTER COLUMN ord_id DROP DEFAULT;
       public          postgres    false    226    225    226            7           2604    20818 
   ram ram_id    DEFAULT     h   ALTER TABLE ONLY public.ram ALTER COLUMN ram_id SET DEFAULT nextval('public.ram_ram_id_seq'::regclass);
 9   ALTER TABLE public.ram ALTER COLUMN ram_id DROP DEFAULT;
       public          postgres    false    218    217    218            �          0    20875    cart 
   TABLE DATA           9   COPY public.cart (cart_id, cart_qty, inv_id) FROM stdin;
    public          postgres    false    224   B       �          0    20808    cpu 
   TABLE DATA           >   COPY public.cpu (cpu_id, name, price, core_count) FROM stdin;
    public          postgres    false    216   B       �          0    20829 	   inventory 
   TABLE DATA           X   COPY public.inventory (inv_id, inv_pc_part, inv_qty, cpu_id, ram_id, mb_id) FROM stdin;
    public          postgres    false    222   EB       �          0    20822    motherboard 
   TABLE DATA           F   COPY public.motherboard (mb_id, name, price, form_factor) FROM stdin;
    public          postgres    false    220   �B       �          0    21023    ordered_items 
   TABLE DATA           ~   COPY public.ordered_items (ord_id, cart_id, ord_date, cust_name, prod_name, pc_part, prod_price, quantity, total) FROM stdin;
    public          postgres    false    226   �B       �          0    20815    ram 
   TABLE DATA           8   COPY public.ram (ram_id, name, price, size) FROM stdin;
    public          postgres    false    218   �C       �           0    0    cart_cart_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.cart_cart_id_seq', 67, true);
          public          postgres    false    223            �           0    0    cpu_cpu_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.cpu_cpu_id_seq', 34, true);
          public          postgres    false    215            �           0    0    inventory_inv_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.inventory_inv_id_seq', 59, true);
          public          postgres    false    221            �           0    0    motherboard_mb_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.motherboard_mb_id_seq', 14, true);
          public          postgres    false    219            �           0    0    ordered_items_ord_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.ordered_items_ord_id_seq', 10, true);
          public          postgres    false    225            �           0    0    ram_ram_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.ram_ram_id_seq', 13, true);
          public          postgres    false    217            F           2606    20881    cart cart_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.cart
    ADD CONSTRAINT cart_pkey PRIMARY KEY (cart_id);
 8   ALTER TABLE ONLY public.cart DROP CONSTRAINT cart_pkey;
       public            postgres    false    224            >           2606    20813    cpu cpu_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.cpu
    ADD CONSTRAINT cpu_pkey PRIMARY KEY (cpu_id);
 6   ALTER TABLE ONLY public.cpu DROP CONSTRAINT cpu_pkey;
       public            postgres    false    216            D           2606    20834    inventory inventory_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.inventory
    ADD CONSTRAINT inventory_pkey PRIMARY KEY (inv_id);
 B   ALTER TABLE ONLY public.inventory DROP CONSTRAINT inventory_pkey;
       public            postgres    false    222            B           2606    20827    motherboard motherboard_pkey 
   CONSTRAINT     ]   ALTER TABLE ONLY public.motherboard
    ADD CONSTRAINT motherboard_pkey PRIMARY KEY (mb_id);
 F   ALTER TABLE ONLY public.motherboard DROP CONSTRAINT motherboard_pkey;
       public            postgres    false    220            H           2606    21028     ordered_items ordered_items_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.ordered_items
    ADD CONSTRAINT ordered_items_pkey PRIMARY KEY (ord_id);
 J   ALTER TABLE ONLY public.ordered_items DROP CONSTRAINT ordered_items_pkey;
       public            postgres    false    226            @           2606    20820    ram ram_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.ram
    ADD CONSTRAINT ram_pkey PRIMARY KEY (ram_id);
 6   ALTER TABLE ONLY public.ram DROP CONSTRAINT ram_pkey;
       public            postgres    false    218            N           2620    20857    cpu trg_cpu_after_insert    TRIGGER     |   CREATE TRIGGER trg_cpu_after_insert AFTER INSERT ON public.cpu FOR EACH ROW EXECUTE FUNCTION public.fnc_cpu_after_insert();
 1   DROP TRIGGER trg_cpu_after_insert ON public.cpu;
       public          postgres    false    216    227            P           2620    20861    motherboard trg_mb_after_insert    TRIGGER     �   CREATE TRIGGER trg_mb_after_insert AFTER INSERT ON public.motherboard FOR EACH ROW EXECUTE FUNCTION public.fnc_mb_after_insert();
 8   DROP TRIGGER trg_mb_after_insert ON public.motherboard;
       public          postgres    false    220    228            O           2620    20859    ram trg_ram_after_insert    TRIGGER     |   CREATE TRIGGER trg_ram_after_insert AFTER INSERT ON public.ram FOR EACH ROW EXECUTE FUNCTION public.fnc_ram_after_insert();
 1   DROP TRIGGER trg_ram_after_insert ON public.ram;
       public          postgres    false    218    229            L           2606    20882    cart cart_inv_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.cart
    ADD CONSTRAINT cart_inv_id_fkey FOREIGN KEY (inv_id) REFERENCES public.inventory(inv_id) ON UPDATE CASCADE ON DELETE CASCADE;
 ?   ALTER TABLE ONLY public.cart DROP CONSTRAINT cart_inv_id_fkey;
       public          postgres    false    224    4676    222            I           2606    20835    inventory inventory_cpu_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.inventory
    ADD CONSTRAINT inventory_cpu_id_fkey FOREIGN KEY (cpu_id) REFERENCES public.cpu(cpu_id) ON UPDATE CASCADE ON DELETE CASCADE;
 I   ALTER TABLE ONLY public.inventory DROP CONSTRAINT inventory_cpu_id_fkey;
       public          postgres    false    4670    222    216            J           2606    20845    inventory inventory_mb_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.inventory
    ADD CONSTRAINT inventory_mb_id_fkey FOREIGN KEY (mb_id) REFERENCES public.motherboard(mb_id) ON UPDATE CASCADE ON DELETE CASCADE;
 H   ALTER TABLE ONLY public.inventory DROP CONSTRAINT inventory_mb_id_fkey;
       public          postgres    false    222    220    4674            K           2606    20840    inventory inventory_ram_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.inventory
    ADD CONSTRAINT inventory_ram_id_fkey FOREIGN KEY (ram_id) REFERENCES public.ram(ram_id) ON UPDATE CASCADE ON DELETE CASCADE;
 I   ALTER TABLE ONLY public.inventory DROP CONSTRAINT inventory_ram_id_fkey;
       public          postgres    false    218    222    4672            M           2606    21029 (   ordered_items ordered_items_cart_id_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.ordered_items
    ADD CONSTRAINT ordered_items_cart_id_fkey FOREIGN KEY (cart_id) REFERENCES public.cart(cart_id) ON DELETE SET NULL;
 R   ALTER TABLE ONLY public.ordered_items DROP CONSTRAINT ordered_items_cart_id_fkey;
       public          postgres    false    224    226    4678            �      x������ � �      �      x�36�L.(5�B�=...  �      �   @   x�35����pr�wr�4��!C.SN�P ���"�ej����idVb����� ��      �      x�34��M2�4�t������� "�Q      �   �   x����J�@���<�/�efv7��[�BEj%D街
���"k/���A�hpNs���F�{�����B�F9�OLd�*"��S��`Q�G�>�@<3fȰ�δ�>�ۼE�X����c^WI�8[j�8����M0��A����e�ܼ���\��7��^n�� ��TNbR5�hD3N����p��sp$��M�G35�^'|}}��.�_/�];CD_䆅       �      x�34�,J�5�4�4�����  ,     