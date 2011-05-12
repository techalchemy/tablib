 #   c o d i n g = u t f - 1 6 
 #   f i l e   o p e n p y x l / t e s t s / t e s t _ p r o p s . p y 
 
 #   C o p y r i g h t   ( c )   2 0 1 0   o p e n p y x l 
 #   
 #   P e r m i s s i o n   i s   h e r e b y   g r a n t e d ,   f r e e   o f   c h a r g e ,   t o   a n y   p e r s o n   o b t a i n i n g   a   c o p y 
 #   o f   t h i s   s o f t w a r e   a n d   a s s o c i a t e d   d o c u m e n t a t i o n   f i l e s   ( t h e   " S o f t w a r e " ) ,   t o   d e a l 
 #   i n   t h e   S o f t w a r e   w i t h o u t   r e s t r i c t i o n ,   i n c l u d i n g   w i t h o u t   l i m i t a t i o n   t h e   r i g h t s 
 #   t o   u s e ,   c o p y ,   m o d i f y ,   m e r g e ,   p u b l i s h ,   d i s t r i b u t e ,   s u b l i c e n s e ,   a n d / o r   s e l l 
 #   c o p i e s   o f   t h e   S o f t w a r e ,   a n d   t o   p e r m i t   p e r s o n s   t o   w h o m   t h e   S o f t w a r e   i s 
 #   f u r n i s h e d   t o   d o   s o ,   s u b j e c t   t o   t h e   f o l l o w i n g   c o n d i t i o n s : 
 # 
 #   T h e   a b o v e   c o p y r i g h t   n o t i c e   a n d   t h i s   p e r m i s s i o n   n o t i c e   s h a l l   b e   i n c l u d e d   i n 
 #   a l l   c o p i e s   o r   s u b s t a n t i a l   p o r t i o n s   o f   t h e   S o f t w a r e . 
 # 
 #   T H E   S O F T W A R E   I S   P R O V I D E D   " A S   I S " ,   W I T H O U T   W A R R A N T Y   O F   A N Y   K I N D ,   E X P R E S S   O R 
 #   I M P L I E D ,   I N C L U D I N G   B U T   N O T   L I M I T E D   T O   T H E   W A R R A N T I E S   O F   M E R C H A N T A B I L I T Y , 
 #   F I T N E S S   F O R   A   P A R T I C U L A R   P U R P O S E   A N D   N O N I N F R I N G E M E N T .   I N   N O   E V E N T   S H A L L   T H E 
 #   A U T H O R S   O R   C O P Y R I G H T   H O L D E R S   B E   L I A B L E   F O R   A N Y   C L A I M ,   D A M A G E S   O R   O T H E R 
 #   L I A B I L I T Y ,   W H E T H E R   I N   A N   A C T I O N   O F   C O N T R A C T ,   T O R T   O R   O T H E R W I S E ,   A R I S I N G   F R O M , 
 #   O U T   O F   O R   I N   C O N N E C T I O N   W I T H   T H E   S O F T W A R E   O R   T H E   U S E   O R   O T H E R   D E A L I N G S   I N 
 #   T H E   S O F T W A R E . 
 # 
 #   @ l i c e n s e :   h t t p : / / w w w . o p e n s o u r c e . o r g / l i c e n s e s / m i t - l i c e n s e . p h p 
 #   @ a u t h o r :   E r i c   G a z o n i 
 
 #   P y t h o n   s t d l i b   i m p o r t s 
 f r o m   _ _ f u t u r e _ _   i m p o r t   w i t h _ s t a t e m e n t 
 f r o m   z i p f i l e   i m p o r t   Z i p F i l e ,   Z I P _ D E F L A T E D 
 f r o m   d a t e t i m e   i m p o r t   d a t e t i m e 
 i m p o r t   o s . p a t h 
 
 #   3 r d   p a r t y   i m p o r t s 
 f r o m   n o s e . t o o l s   i m p o r t   e q _ 
 
 #   p a c k a g e   i m p o r t s 
 f r o m   o p e n p y x l . t e s t s . h e l p e r   i m p o r t   D A T A D I R ,   T M P D I R ,   m a k e _ t m p d i r ,   c l e a n _ t m p d i r ,   \ 
                 a s s e r t _ e q u a l s _ f i l e _ c o n t e n t 
 f r o m   o p e n p y x l . r e a d e r . w o r k b o o k   i m p o r t   r e a d _ p r o p e r t i e s _ c o r e ,   \ 
                 r e a d _ s h e e t s _ t i t l e s ,   g e t _ n u m b e r _ o f _ p a r t s 
 f r o m   o p e n p y x l . w r i t e r . w o r k b o o k   i m p o r t   w r i t e _ p r o p e r t i e s _ c o r e ,   \ 
                 w r i t e _ p r o p e r t i e s _ a p p 
 f r o m   o p e n p y x l . s h a r e d . o o x m l   i m p o r t   A R C _ A P P ,   A R C _ C O R E 
 f r o m   o p e n p y x l . w o r k b o o k   i m p o r t   D o c u m e n t P r o p e r t i e s ,   W o r k b o o k 
 
 
 c l a s s   T e s t R e a d e r P r o p s ( o b j e c t ) : 
 
         @ c l a s s m e t h o d 
         d e f   s e t u p _ c l a s s ( c l s ) : 
                 c l s . g e n u i n e _ f i l e n a m e   =   o s . p a t h . j o i n ( D A T A D I R ,   ' g e n u i n e ' ,   ' e m p t y . x l s x ' ) 
                 c l s . a r c h i v e   =   Z i p F i l e ( c l s . g e n u i n e _ f i l e n a m e ,   ' r ' ,   Z I P _ D E F L A T E D ) 
 
         @ c l a s s m e t h o d 
         d e f   t e a r d o w n _ c l a s s ( c l s ) : 
                 c l s . a r c h i v e . c l o s e ( ) 
 
         d e f   t e s t _ r e a d _ p r o p e r t i e s _ c o r e ( s e l f ) : 
                 c o n t e n t   =   s e l f . a r c h i v e . r e a d ( A R C _ C O R E ) 
                 p r o p   =   r e a d _ p r o p e r t i e s _ c o r e ( c o n t e n t ) 
                 e q _ ( p r o p . c r e a t o r ,   ' * . * ' ) 
                 e q _ ( p r o p . l a s t _ m o d i f i e d _ b y ,   ' A u r � l i e n   C a m p � a s ' ) 
                 e q _ ( p r o p . c r e a t e d ,   d a t e t i m e ( 2 0 1 0 ,   4 ,   9 ,   2 0 ,   4 3 ,   1 2 ) ) 
                 e q _ ( p r o p . m o d i f i e d ,   d a t e t i m e ( 2 0 1 1 ,   2 ,   9 ,   1 3 ,   4 9 ,   3 2 ) ) 
 
         d e f   t e s t _ r e a d _ s h e e t s _ t i t l e s ( s e l f ) : 
                 c o n t e n t   =   s e l f . a r c h i v e . r e a d ( A R C _ A P P ) 
                 s h e e t _ t i t l e s   =   r e a d _ s h e e t s _ t i t l e s ( c o n t e n t ) 
                 e q _ ( s h e e t _ t i t l e s ,   \ 
                                 [ ' S h e e t 1   -   T e x t ' ,   ' S h e e t 2   -   N u m b e r s ' ,   ' S h e e t 3   -   F o r m u l a s ' ,   ' S h e e t 4   -   D a t e s ' ] ) 
 
 
 c l a s s   T e s t R e a d e r P r o p s M i x e d ( o b j e c t ) : 
 
         @ c l a s s m e t h o d 
         d e f   s e t u p _ c l a s s ( c l s ) : 
                 r e f e r e n c e _ f i l e n a m e   =   \ 
                                 o s . p a t h . j o i n ( D A T A D I R ,   ' r e a d e r ' ,   ' a p p - m u l t i - t i t l e s . x m l ' ) 
                 w i t h   o p e n ( r e f e r e n c e _ f i l e n a m e )   a s   h a n d l e : 
                         c l s . c o n t e n t   =   h a n d l e . r e a d ( ) 
 
         d e f   t e s t _ r e a d _ s h e e t _ t i t l e s _ m i x e d ( s e l f ) : 
                 s h e e t _ t i t l e s   =   r e a d _ s h e e t s _ t i t l e s ( s e l f . c o n t e n t ) 
                 e q _ ( s h e e t _ t i t l e s , 
                                 [ ' T o C ' ,   ' C o n t r a c t Y e a r ' ,   ' C o n t r a c t T i e r ' ,   ' D e m a n d ' , 
                                 ' L i n e a r i z e d F u n c t i o n ' ,   ' M a r k e t ' ,   ' T r a n s m i s s i o n ' ] ) 
 
         d e f   t e s t _ n u m b e r _ o f _ p a r t s ( s e l f ) : 
                 p a r t s _ n u m b e r   =   g e t _ n u m b e r _ o f _ p a r t s ( s e l f . c o n t e n t ) 
                 e q _ ( p a r t s _ n u m b e r , 
                                 ( { ' W o r k s h e e t s ' :   7 ,   ' N a m e d   R a n g e s ' :   7 } , 
                                 [ ' W o r k s h e e t s ' ,   ' N a m e d   R a n g e s ' ] ) ) 
 
 
 c l a s s   T e s t W r i t e P r o p s ( o b j e c t ) : 
 
         @ c l a s s m e t h o d 
         d e f   s e t u p _ c l a s s ( c l s ) : 
                 m a k e _ t m p d i r ( ) 
                 c l s . t m p _ f i l e n a m e   =   o s . p a t h . j o i n ( T M P D I R ,   ' t e s t . x l s x ' ) 
                 c l s . p r o p   =   D o c u m e n t P r o p e r t i e s ( ) 
 
         @ c l a s s m e t h o d 
         d e f   t e a r d o w n _ c l a s s ( c l s ) : 
                 c l e a n _ t m p d i r ( ) 
 
         d e f   t e s t _ w r i t e _ p r o p e r t i e s _ c o r e ( s e l f ) : 
                 s e l f . p r o p . c r e a t o r   =   ' T E S T _ U S E R ' 
                 s e l f . p r o p . l a s t _ m o d i f i e d _ b y   =   ' S O M E B O D Y ' 
                 s e l f . p r o p . c r e a t e d   =   d a t e t i m e ( 2 0 1 0 ,   4 ,   1 ,   2 0 ,   3 0 ,   0 0 ) 
                 s e l f . p r o p . m o d i f i e d   =   d a t e t i m e ( 2 0 1 0 ,   4 ,   5 ,   1 4 ,   5 ,   3 0 ) 
                 c o n t e n t   =   w r i t e _ p r o p e r t i e s _ c o r e ( s e l f . p r o p ) 
                 a s s e r t _ e q u a l s _ f i l e _ c o n t e n t ( 
                                 o s . p a t h . j o i n ( D A T A D I R ,   ' w r i t e r ' ,   ' e x p e c t e d ' ,   ' c o r e . x m l ' ) , 
                                 c o n t e n t ) 
 
         d e f   t e s t _ w r i t e _ p r o p e r t i e s _ a p p ( s e l f ) : 
                 w b   =   W o r k b o o k ( ) 
                 w b . c r e a t e _ s h e e t ( ) 
                 w b . c r e a t e _ s h e e t ( ) 
                 c o n t e n t   =   w r i t e _ p r o p e r t i e s _ a p p ( w b ) 
                 a s s e r t _ e q u a l s _ f i l e _ c o n t e n t ( 
                                 o s . p a t h . j o i n ( D A T A D I R ,   ' w r i t e r ' ,   ' e x p e c t e d ' ,   ' a p p . x m l ' ) , 
                                 c o n t e n t ) 
