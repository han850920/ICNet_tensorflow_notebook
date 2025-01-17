import tensorflow as tf
class ICNet_BN(tf.keras.Model):
    def __init__(self, cfg, mode,image_reader):
        self.cfg = cfg
        self.scale = cfg.filter_scale
        self.is_training = cfg.filter_scale
        self.mode = mode
        self.image_reader = image_reader
        super(ICNet_BN,self).__init__(name='')
        # remember to add activation function in call()
        self.conv1_1_3x3_s2 = tf.keras.layers.Conv2D(32,(3,3),strides=(2,2),use_bias=False,padding='VALID')
        self.conv1_1_3x3_s2_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv1_2_3x3 = tf.keras.layers.Conv2D(32,(3,3),strides=(1,1),use_bias=False,padding='VALID')
        self.conv1_2_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv1_3_3x3 = tf.keras.layers.Conv2D(64,(3,3),strides=(1,1),use_bias=False,padding='VALID')
        self.conv1_3_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding0 = tf.keras.layers.ZeroPadding2D()
        self.pool1_3x3_s2 = tf.keras.layers.MaxPool2D()
        self.conv2_1_1x1_proj = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv2_1_1x1_proj_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv2_1_1x1_reduce = tf.keras.layers.Conv2D(32,(1,1),strides=(1,1),use_bias=False,padding='same')
        self.conv2_1_1x1_reduce_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding1 = tf.keras.layers.ZeroPadding2D()
        self.conv2_1_3x3 = tf.keras.layers.Conv2D(32,(3,3),strides=(1,1),use_bias=False,padding='VALID')
        self.conv2_1_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv2_1_1x1_increase = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv2_1_1x1_increase_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv2_1 = tf.keras.layers.Add()
        self.conv2_1_relu = tf.keras.layers.ReLU()
        self.conv2_2_1x1_reduce = tf.keras.layers.Conv2D(32,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv2_2_1x1_reduce_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding2 = tf.keras.layers.ZeroPadding2D()
        self.conv2_2_3x3 = tf.keras.layers.Conv2D(32,(3,3),strides=(1,1),use_bias=False,padding='VALID')
        self.conv2_2_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv2_2_1x1_increase = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv2_2_1x1_increase_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv2_2 = tf.keras.layers.Add()
        self.conv2_2_relu = tf.keras.layers.ReLU()
        self.conv2_3_1x1_reduce = tf.keras.layers.Conv2D(32,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv2_3_1x1_reduce_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding3 = tf.keras.layers.ZeroPadding2D()
        self.conv2_3_3x3 = tf.keras.layers.Conv2D(32,(3,3),strides=(1,1),use_bias=False,padding='VALID')
        self.conv2_3_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv2_3_1x1_increase = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv2_3_1x1_increase_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv2_3 = tf.keras.layers.Add()
        self.conv2_3_relu = tf.keras.layers.ReLU()
        self.conv3_1_1x1_proj = tf.keras.layers.Conv2D(256,(1,1),strides=(2,2),use_bias=False,padding='VALID')
        self.conv3_1_1x1_proj_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv3_1_1x1_reduce = tf.keras.layers.Conv2D(64,(1,1),strides=(2,2),use_bias=False,padding='VALID')
        self.conv3_1_1x1_reduce_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding4 = tf.keras.layers.ZeroPadding2D()
        self.conv3_1_3x3 = tf.keras.layers.Conv2D(64,(3,3),strides=(1,1),use_bias=False,padding='VALID')
        self.conv3_1_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv3_1_1x1_increase = tf.keras.layers.Conv2D(64,(3,3),strides=(1,1),use_bias=False,padding='VALID')
        self.conv3_1_1x1_increase_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv3_1 = tf.keras.layers.Add()
        self.conv3_1_relu = tf.keras.layers.ReLU()
        self.conv3_2_1x1_reduce = tf.keras.layers.Conv2D(64,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv3_2_1x1_reduce_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding5 = tf.keras.layers.ZeroPadding2D()
        self.conv3_2_3x3 = tf.keras.layers.Conv2D(64,(3,3),strides=(1,1),use_bias=False,padding='VALID')
        self.conv3_2_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv3_2_1x1_increase = tf.keras.layers.Conv2D(256,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv3_2_1x1_increase_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv3_2 = tf.keras.layers.Add()
        self.conv3_2_relu = tf.keras.layers.ReLU()
        self.conv3_3_1x1_reduce = tf.keras.layers.Conv2D(64,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv3_3_1x1_reduce_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding6 = tf.keras.layers.ZeroPadding2D()
        self.conv3_3_3x3 = tf.keras.layers.Conv2D(64,(3,3),strides=(1,1),use_bias=False,padding='VALID')
        self.conv3_3_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv3_3_1x1_increase = tf.keras.layers.Conv2D(256,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv3_3_1x1_increase_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv3_3 = tf.keras.layers.Add()
        self.conv3_3_relu = tf.keras.layers.ReLU()
        self.conv3_4_1x1_reduce = tf.keras.layers.Conv2D(64,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv3_4_1x1_reduce_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding7 = tf.keras.layers.ZeroPadding2D()
        self.conv3_4_3x3 = tf.keras.layers.Conv2D(64,(3,3),strides=(1,1),use_bias=False,padding='VALID')
        self.conv3_4_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv3_4_1x1_increase = tf.keras.layers.Conv2D(256,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv3_4_1x1_increase_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv3_4 = tf.keras.layers.Add()
        self.conv3_4_relu = tf.keras.layers.ReLU()
        self.conv4_1_1x1_proj = tf.keras.layers.Conv2D(512,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv4_1_1x1_proj_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv4_1_1x1_reduce = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv4_1_1x1_proj_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding8 = tf.keras.layers.ZeroPadding2D()
        self.conv4_1_3x3 = tf.keras.layers.Conv2D(128,(3,3),dilation_rate=(2,2),use_bias=False,padding='VALID')
        self.conv4_1_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv4_1_1x1_increase = tf.keras.layers.Conv2D(512,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv4_1_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv4_1 = tf.keras.layers.Add()
        self.conv4_1_relu = tf.keras.layers.ReLU()
        self.conv4_2_1x1_reduce = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv4_2_1x1_reduce_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding9 = tf.keras.layers.ZeroPadding2D()
        self.conv4_2_3x3 = tf.keras.layers.Conv2D(128,(3,3),dilation_rate=(2,2),use_bias=False,padding='VALID')
        self.conv4_2_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv4_2_1x1_increase = tf.keras.layers.Conv2D(512,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv4_2_1x1_increase_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv4_2 = tf.keras.layers.Add()
        self.conv4_2_relu = tf.keras.layers.ReLU()
        self.conv4_3_1x1_reduce = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv4_3_1x1_reduce_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding10 = tf.keras.layers.ZeroPadding2D()
        self.conv4_3_3x3 = tf.keras.layers.Conv2D(128,(3,3),dilation_rate=(2,2),use_bias=False,padding='VALID')
        self.conv4_3_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv4_3_1x1_increase = tf.keras.layers.Conv2D(512,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv4_3_1x1_increase_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv4_3 = tf.keras.layers.Add()
        self.conv4_3_relu = tf.keras.layers.ReLU()
        self.conv4_4_1x1_reduce = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv4_4_1x1_reduce_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding11 = tf.keras.layers.ZeroPadding2D()
        self.conv4_4_3x3 = tf.keras.layers.Conv2D(128,(3,3),dilation_rate=(2,2),use_bias=False,padding='VALID')
        self.conv4_4_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv4_4_1x1_increase = tf.keras.layers.Conv2D(512,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv4_4_1x1_increase_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv4_4 = tf.keras.layers.Add()
        self.conv4_4_relu = tf.keras.layers.ReLU()
        self.conv4_5_1x1_reduce = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv4_5_1x1_reduce_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding12 = tf.keras.layers.ZeroPadding2D()
        self.conv4_5_3x3 = tf.keras.layers.Conv2D(128,(3,3),dilation_rate=(2,2),use_bias=False,padding='VALID')
        self.conv4_5_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv4_5_1x1_increase = tf.keras.layers.Conv2D(512,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv4_5_1x1_increase_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv4_5 = tf.keras.layers.Add()
        self.conv4_5_relu = tf.keras.layers.ReLU()
        self.conv4_6_1x1_reduce = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv4_6_1x1_reduce_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding13 = tf.keras.layers.ZeroPadding2D()
        self.conv4_6_3x3 = tf.keras.layers.Conv2D(128,(3,3),dilation_rate=(2,2),use_bias=False,padding='VALID')
        self.conv4_6_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv4_6_1x1_increase = tf.keras.layers.Conv2D(512,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv4_6_1x1_increase_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv4_6 = tf.keras.layers.Add()
        self.conv4_6_relu = tf.keras.layers.ReLU()
        self.conv5_1_1x1_proj = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv5_1_1x1_proj_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv5_1_1x1_reduce = tf.keras.layers.Conv2D(256,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv5_1_1x1_reduce_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding14 = tf.keras.layers.ZeroPadding2D()
        self.conv5_1_3x3 = tf.keras.layers.Conv2D(256,(3,3),dilation_rate=(4,4),use_bias=False,padding='VALID')
        self.conv5_1_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv5_1_1x1_increase = tf.keras.layers.Conv2D(1024,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv5_1_1x1_increase_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv5_1 = tf.keras.layers.Add()
        self.conv5_1_relu = tf.keras.layers.ReLU()
        self.conv5_2_1x1_reduce = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv5_2_1x1_reduce_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding15 = tf.keras.layers.ZeroPadding2D()
        self.conv5_2_3x3 = tf.keras.layers.Conv2D(128,(3,3),dilation_rate=(2,2),use_bias=False,padding='VALID')
        self.conv5_2_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv5_2_1x1_increase = tf.keras.layers.Conv2D(512,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv5_2_1x1_increase_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)

        self.conv5_2 = tf.keras.layers.Add()
        self.conv5_2_relu = tf.keras.layers.ReLU()
        self.conv5_3_1x1_reduce = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv5_3_1x1_reduce_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding16 = tf.keras.layers.ZeroPadding2D()
        self.conv5_3_3x3 = tf.keras.layers.Conv2D(128,(3,3),dilation_rate=(2,2),use_bias=False,padding='VALID')
        self.conv5_3_3x3_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv5_3_1x1_increase = tf.keras.layers.Conv2D(512,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv5_3_1x1_increase_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv5_3 = tf.keras.layers.Add()
        self.conv5_3_relu = tf.keras.layers.ReLU()
        
        self.conv5_3_pool1 = tf.keras.layers.AveragePooling2D()
        self.conv5_3_pool2 = tf.keras.layers.AveragePooling2D()
        self.conv5_3_pool3 = tf.keras.layers.AveragePooling2D()
        self.conv5_3_pool6 = tf.keras.layers.AveragePooling2D()
        
        self.conv5_3_sum = tf.keras.layers.Add()
        self.conv5_4_k1 = tf.keras.layers.Conv2D(256,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv5_4_k1_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.padding17 = tf.keras.layers.ZeroPadding2D()
        self.conv_sub4 = tf.keras.layers.Conv2D(128,(3,3),dilation_rate=(2,2),use_bias=False,padding='VALID')
        self.conv_sub4_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv3_1_sub2_proj = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv3_1_sub2_proj_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.sub24_sum = tf.keras.layers.Add()
        self.conv5_3_relu = tf.keras.layers.ReLU()
        self.padding18 = tf.keras.layers.ZeroPadding2D()
        self.conv_sub2 = tf.keras.layers.Conv2D(128,(3,3),dilation_rate=(2,2),use_bias=False,padding='SAME')
        self.conv_sub2_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        
        self.conv1_sub1 = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='SAME')
        self.conv1_sub1_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv2_sub1 = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='SAME')
        self.conv2_sub1_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv3_sub1 = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='SAME')
        self.conv3_sub1_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)
        self.conv3_sub1_proj = tf.keras.layers.Conv2D(128,(1,1),strides=(1,1),use_bias=False,padding='VALID')
        self.conv3_sub1_proj_bn = tf.keras.layers.BatchNormalization(momentum=0.95, epsilon=1e-5)

        self.sub12_sum = tf.keras.layers.Add()
        self.sub12_sum_relu = tf.keras.layers.ReLU()
        self.conv6_cls = tf.keras.layers.Conv2D(self.cfg.params['num_classes'],(1,1),strides=(1,1),use_bias=False,padding='VALID')
    
        self.sub4_out = tf.keras.layers.Conv2D(self.cfg.params['num_classes'],(1,1),strides=(1,1),use_bias=False,padding='VALID')
        
        self.sub24_out = tf.keras.layers.Conv2D(self.cfg.params['num_classes'],(1,1),strides=(1,1),use_bias=False,padding='VALID')
    
    def interp(self, input, s_factor=1, z_factor=1, name=None):
        ori_h, ori_w = input.get_shape().as_list()[1:3]
        # shrink
        ori_h = (ori_h - 1) * s_factor + 1
        ori_w = (ori_w - 1) * s_factor + 1
        # zoom
        ori_h = ori_h + (ori_h - 1) * (z_factor - 1)
        ori_w = ori_w + (ori_w - 1) * (z_factor - 1)
        resize_shape = [int(ori_h), int(ori_w)]
        
        return tf.compat.v1.image.resize_bilinear(input, size=resize_shape, align_corners=True, name=name)
    
    def call(self,input_tensor,training=False):
        #1
        x = self.interp(input_tensor,s_factor=0.5)
        print(x.shape)
        x = self.conv1_1_3x3_s2(x)
        x = self.conv1_1_3x3_s2_bn(x,training=self.is_training)
        x = tf.nn.relu(x)
        x = self.conv1_2_3x3(x)
        x = self.conv1_2_3x3_bn(x,training=self.is_training)
        x = tf.nn.relu(x)
        x = self.conv1_3_3x3(x)
        x = self.conv1_3_3x3_bn(x,training=self.is_training)
        x = tf.nn.relu(x)
        x = self.padding0(x,padding=(1,1))
        x = self.pool1_3x3_s2(x,pool_size=(3,3),strides=(2,2))
        x1 = self.conv2_1_1x1_proj(x)          
        x2 = self.conv2_1_1x1_proj_bn(x1,  training=self.is_training)
        
        #2
        x3 = self.conv2_1_1x1_reduce(x1)
        x3 = self.conv2_1_1x1_reduce_bn(x3)
        x3 = tf.nn.relu(x3)
        x3 = self.padding1(x3,padding=(1,1))
        x3 = self.conv2_1_3x3(x3)
        x3 = self.conv2_1_3x3_bn(x3,training=self.is_training)
        x3 = tf.nn.relu(x3)
        x3 = self.conv2_1_1x1_increase(x3)
        x3 = self.conv2_1_1x1_increase_bn(x3,training=self.is_training)

        #3
        x2 = tf.image.resize(x2, size=tf.shape(x3)[1:3], method=tf.image.ResizeMethod.BILINEAR,)
        x4 = self.conv2_1([x2,x3])
        x4 = self.conv2_1_relu(x4)
        x5 = self.conv2_2_1x1_reduce(x4)
        x5 = self.conv2_2_1x1_reduce_bn(x5,  training=self.is_training)
        x5 = self.padding2(x5,padding=(1,1))
        x5 = self.conv2_2_3x3(x5)
        x5 = self.conv2_2_3x3_bn(x5,training=self.is_training)
        x5 = self.conv2_2_1x1_increase(x5)
        x5 = self.conv2_2_1x1_increase_bn(x5,  training=self.is_training)
        
        #4
        x4 = tf.image.resize(x4, size=tf.shape(x5)[1:3], method=tf.image.ResizeMethod.BILINEAR)
        x6 = self.conv2_1([x4, x5])
        x6 = self.conv2_2_relu(x6)
        x7 = self.conv2_3_1x1_reduce(x6)
        x7 = self.conv2_3_1x1_reduce_bn(x7,  training=self.is_training)
        x7 = tf.nn.relu(x7)
        x7 = self.padding3(x7,padding=(1,1))
        x7 = self.conv2_3_3x3(x7)
        x7 = self.conv2_3_3x3_bn(x7,  training=self.is_training)
        x7 = tf.nn.relu(x7)
        x7 = self.conv2_3_1x1_increase(x7)
        x7 = self.conv2_3_1x1_increase_bn(x7,  training=self.is_training)
        
        #5
        x6 = tf.image.resize(x6, size=tf.shape(x7)[1:3], method=tf.image.ResizeMethod.BILINEAR)
        x8 = self.conv2_3([x6,x7])
        x8 = self.conv2_3_relu(x8)                                 
        x9 = self.conv3_1_1x1_proj(x8)
        x9 = self.conv3_1_1x1_proj_bn(x9,  training=self.is_training)
        
        x10 = self.conv3_1_1x1_reduce(x8)
        x10 = self.conv3_1_1x1_reduce_bn(x10,  training=self.is_training)
        x10 = tf.nn.relu(x10)
        x10 = self.padding4(x10,pading=(1,1))
        x10 = self.conv3_1_3x3(x10)
        x10 = self.conv3_1_3x3_bn(x10)
        x10 = tf.nn.relu(x10)
        x10 = self.conv3_1_1x1_increase(x10)
        x10 = self.conv3_1_1x1_increase_bn(x10)
                                          
        x9 = tf.image.resize(x9,size=tf.shape(x10)[1:3], method=tf.image.ResizeMethod.BILINEAR)
        x11 = self.conv3_1([x9,x10])
        x11 = self.conv3_1_relu(x11)
        x12 = self.interp(x11,s_factor=0.5)
        x13 = self.conv3_2_1x1_reduce(x12)
        x13 = self.conv3_2_1x1_reduce_bn(x13,  training=self.is_training)
        x13 = tf.nn.relu(x13)
        x13 = self.padding5(x13,padding=(1,1))
        x13 = self.conv3_2_3x3(x13)
        x13 = self.conv3_2_3x3_bn(x13,  training=self.is_training)
        x13 = tf.nn.relu(x13)
        x13 = self.conv3_2_1x1_increase(x13)
        x13 = self.conv3_2_1x1_increase_bn(x13,  training=self.is_training)
                                          
        x12 = tf.image.resize(x12,size=tf.shape(x13)[1:3], method=tf.image.ResizeMethod.BILINEAR)
        x14 = self.conv3_2([x12,x14])
        x14 = self.conv3_2_relu(x14)
        x15 = self.conv3_3_1x1_reduce(x14)
        x15 = self.conv3_3_1x1_reduce_bn(x15,  training=self.is_training) 
        x15 = tf.nn.relu(x15)
        x15 = self.padding6(x15,padding=(1,1))
        x15 = self.conv3_3_3x3(x15)
        x15 = self.conv3_3_3x3_bn(x15,  training=self.is_training)
        x15 = tf.nn.relu(x15)
        x15 = self.conv3_3_1x1_increase(x15)
        x15 = self.conv3_3_1x1_increase_bn(x15,  training=self.is_training)
                   
        x14 = tf.image.resize(x14,size=tf.shape(x15)[1:3], method=tf.image.ResizeMethod.BILINEAR)
        x16 = self.conv3_3([x14,x15]) 
        x16 = self.conv3_3_relu(x16)
        x17 = self.conv3_4_1x1_reduce(x16)
        x17 = self.conv3_4_1x1_reduce_bn(x17,  training=self.is_training)
        x17 = tf.nn.relu(x17)
        x17 = self.padding7(x17,padding=(1,1))
        x17 = self.conv3_4_3x3(x17)
        x17 = self.conv3_4_3x3_bn(x17,  training=self.is_training)
        x17 = tf.nn.relu(x17)
        x17 = self.conv3_4_1x1_increase(x17)
        x17 = self.conv3_4_1x1_increase_bn(x17,  training=self.is_training)
                                          
        x16 = tf.image.resize(x16,size=tf.shape(x17)[1:3], method=tf.image.ResizeMethod.BILINEAR)
        x18 = self.conv3_4([x16,x17])
        x18 = self.conv3_4_relu(x18)
        x19 = self.conv4_1_1x1_proj(x18)
        x19 = self.conv4_1_1x1_proj_bn(x19,  training=self.is_training)
      
        x18 = self.conv4_1_1x1_reduce(x18)
        x18 = self.conv4_1_1x1_reduce_bn(x18,  training=self.is_training)
        x18 = tf.nn.relu(x18)
        x18 = self.padding8(x18,padding=(2,2))
        x18 = self.conv4_1_3x3(x18)
        x18 = self.conv4_1_3x3_bn(x18,  training=self.is_training)
        x18 = tf.nn.relu(x18)
        x18 = self.conv4_1_1x1_increase(x18)
        x18 = self.conv4_1_1x1_increase_bn(x18)
       
                                          
        x19 = tf.image.resize(x19,size=tf.shape(x18)[1:3], method=tf.image.ResizeMethod.BILINEAR)
        x20 = self.conv4_1([x19,x18])
        x20 = self.conv4_1_relu(x20)
        x21 = self.conv4_2_1x1_reduce(x20)
        x21 = self.conv4_2_1x1_reduce_bn(x21,  training=self.is_training)
        x21 = tf.nn.relu(x21)
        x21 = self.padding9(x21,padding=(2,2))
        x21 = self.conv4_2_3x3(x21)
        x21 = self.conv4_2_3x3_bn(x21,  training=self.is_training)
        x21 = tf.nn.relu(x21)
        x21 = self.conv4_2_1x1_increase(x21)
        x21 = self.conv4_2_1x1_increase_bn(x21)
                                          
        x20 = tf.image.resize(x20,size=tf.shape(x21)[1:3], method=tf.image.ResizeMethod.BILINEAR)
        x22 = self.conv4_2([x20,x21])
        x22 = self.conv4_2_relu(x22)
        x23 = self.conv4_3_1x1_reduce(x22)
        x23 = self.conv4_3_1x1_reduce_bn(x23,  training=self.is_training)
        x23 = tf.nn.relu(x23)
        x23 = self.padding10(x23,padding=(2,2))
        x23 = self.conv4_3_3x3(x23)
        x23 = self.conv4_3_3x3_bn(x23,  training=self.is_training)
        x23 = tf.nn.relu(x23)
        x23 = self.conv4_3_1x1_increase(x23)
        x23 = self.conv4_3_1x1_increase_bn(x23)
                      
        x22 = tf.image.resize(x22,size=tf.shape(x23)[1:3], method=tf.image.ResizeMethod.BILINEAR)
        x24 = self.conv4_3([x22,x23])
        x24 = self.conv4_3_relu(x24)
        x25 = self.conv4_4_1x1_reduce(x24)
        x25 = self.conv4_4_1x1_reduce_bn(x25,  training=self.is_training)
        x25 = tf.nn.relu(x25)
        x25 = self.padding11(x25,padding=(2,2))
        x25 = self.conv4_4_3x3(x25)
        x25 = self.conv4_4_3x3_bn(x25,  training=self.is_training)
        x25 = tf.nn.relu(x25)
        x25 = self.conv4_4_1x1_increase(x25)
        x25 = self.conv4_4_1x1_increase_bn(x25,  training=self.is_training)
                  
        x24 = tf.image.resize(x24,size=tf.shape(x25)[1:3], method=tf.image.ResizeMethod.BILINEAR)
        x26 = self.conv4_4([x24,x25])
        x26 = self.conv4_4_relu(x26)
        x27 = self.conv4_5_1x1_reduce(x26)
        x27 = self.conv4_5_1x1_reduce_bn(x27,  training=self.is_training)
        x27 = tf.nn.relu(x27)
        x27 = self.conv4_5_3x3(x27)
        x27 = self.conv4_5_3x3_bn(x27,  training=self.is_training)
        x27 = tf.nn.relu(x27)
        x27 = self.conv4_5_1x1_increase(x27)
        x27 = self.conv4_5_1x1_increase_bn(x27,  training=self.is_training)
      
        x26 = tf.image.resize(x26,size=tf.shape(x27)[1:3], method=tf.image.ResizeMethod.BILINEAR)
        x28 = self.conv4_5([x26,x27])
        x28 = self.conv4_5_relu(x28)
        x29 = self.conv4_6_1x1_reduce(x28)
        x29 = self.conv4_6_1x1_reduce_bn(x28,  training=self.is_training)
        x29 = tf.nn.relu(x28)
        x29 = self.padding13(x28,padding=(2,2))
        x29 = self.conv4_6_3x3(x28)
        x29 = self.conv4_6_3x3_bn(x28,  training=self.is_training)
        x29 = tf.nn.relu(x28)
        x29 = self.conv4_6_1x1_increase(x28)
        x29 = self.conv4_6_1x1_increase_bn(x28,  training=self.is_training)
                    
        x28 = tf.image.resize(x28,size=tf.shape(x29)[1:3], method=tf.image.ResizeMethod.BILINEAR)                                  
        x30 = self.conv4_6([x28,x29])
        x30 = self.conv4_6_relu(x30)
        x31 = self.conv5_1_1x1_proj(x30)
        x31 = self.conv5_1_1x1_proj_bn(x31,  training=self.is_training)
                  
        x30 = self.conv5_1_1x1_reduce(x30)
        x30 = self.conv5_1_1x1_reduce_bn(x30,  training=self.is_training)
        x30 = tf.nn.relu(x30)
        x30 = self.padding14(x30,padding=(4,4))
        x30 = self.conv5_1_3x3(x30)
        x30 = self.conv5_1_3x3_bn(x30,  training=self.is_training)
        x30 = tf.nn.relu(x30)
        x30 = self.conv5_1_1x1_increase(x30)
        x30 = self.conv5_1_1x1_increase_bn(x30,  training=self.is_training)
          
        x31 = tf.image.resize(x31,size=tf.shape(x30)[1:3], method=tf.image.ResizeMethod.BILINEAR)
        x32 = self.conv5_1([x31,x30])
        x32 = self.conv5_1_relu(x32)
        x33 = self.conv5_2_1x1_reduce(x32)
        x33 = self.conv5_2_1x1_reduce_bn(x33,  training=self.is_training)
        x33 = tf.nn.relu(x33)
        x33 = self.padding15(x33,padding=(4,4))
        x33 = self.conv5_2_3x3(x33)
        x33 = self.conv5_2_3x3_bn(x33,  training=self.is_training)
        x33 = tf.nn.relu(x33)
        x33 = self.conv5_2_1x1_increase(x33)
        x33 = self.conv5_2_1x1_increase_bn(x33,  training=self.is_training)
        
        x32 = tf.image.resize(x32,size=tf.shape(x33)[1:3], method=tf.image.ResizeMethod.BILINEAR)
        x34 = self.conv5_2([x32,x33])
        x34 = self.conv5_2_relu(x34)
        x35 = self.conv5_3_1x1_reduce(x34)
        x35 = self.conv5_3_1x1_reduce_bn(x35,  training=self.is_training)
        x35 = self.tf.nn.relu(x35)
        x35 = self.padding16(x35,padding=(4,4))
        x35 = self.conv5_3_3x3(x35)
        x35 = self.conv5_3_3x3_bn(x35,  training=self.is_training)
        x35 = tf.nn.relu(x35)
        x35 = self.conv5_3_1x1_increase(x35)
        x35 = self.conv5_3_1x1_increase_bn(x35,  training=self.is_training)
          
        x34 = tf.image.resize(x34,size=tf.shape(x35)[1:3], method=tf.image.ResizeMethod.BILINEAR)
        x36 = self.conv5_3([x34,x35])
        x36 = self.conv5_3_relu(x36)
        
        shape = x36.get_shape().as_list()[1:3]
        h,w = shape
          
        x37 = self.conv5_3_pool1(x36, pool_size=(h,w),strides=(h,w))
        x37 = tf.image.resize(x37, size=shape, method=tf.image.ResizeMethod.BILINEAR, antialias=True)
        x38 = self.conv5_3_pool1(x36, pool_size=(h/2,w/2),strides=(h/2,w/2))
        x38 = tf.image.resize(x38, size=shape, method=tf.image.ResizeMethod.BILINEAR, antialias=True)
        x39 = self.conv5_3_pool1(x36, pool_size=(h/3,w/3),strides=(h/3,w/3))
        x39 = tf.image.resize(x39, size=shape, method=tf.image.ResizeMethod.BILINEAR, antialias=True)
        x40 = self.conv5_3_pool1(x36, pool_size=(h/4,w/4),strides=(h/4,w/4))
        x40 = tf.image.resize(x40, size=shape, method=tf.image.ResizeMethod.BILINEAR, antialias=True)
        
        x36 = tf.image.resize(x36,size=tf.shape(x40)[1:3], method=tf.image.ResizeMethod.BILINEAR)
        x41 = self.conv5_3_sum([x36,x37,x38,x39,x40])
        x41 = self.conv5_4_k1(x41)
        x41 = self.conv5_4_k1_bn(x41,  training=self.is_training)
        x41 = tf.nn.relu(x41)
        x41 = self.interp(x41, z_factor=2.0)
        x42 = self.padding17(x41,padding=(2,2))
        x42 = self.conv_sub4(x42)
        x42 = self.conv_sub4_bn(x42,  training=self.is_training)
                              
        x43 = self.conv3_1_sub2_proj(x11)
        x43 = self.conv3_1_sub2_proj_bn(x43,   training=self.is_training)
        
        x42 = tf.image.resize(x42,size=tf.shape(x43)[1:3], method=tf.image.ResizeMethod.BILINEAR)
        x44 = self.sub24_sum([x42,x43])  
        x44 = self.sub24_sum_relu(x44)
        x44 = self.interp(x44, z_factor=2.0)
        x45 = self.padding18(x44,padding=(2,2))
        x45 = self.conv_sub2(x45)
        x45 = self.conv_sub2_bn(x45,   training=self.is_training)
                                                                                 
        x46 = self.conv1_sub1(input_tensor)
        x46 = self.conv1_sub1_bn(x46,   training=self.is_training)
        x46 = tf.nn.relu(x46)
        x46 = self.conv2_sub1(x46)
        x46 = self.conv2_sub1_bn(x46,   training=self.is_training)
        x46 = tf.nn.relu(x46)
        x46 = self.conv3_sub1(x46)
        x46 = self.conv3_sub1_bn(x46,   training=self.is_training)          
        x46 = tf.nn.relu(x46)
        x46 = self.conv3_sub1_proj(x46)
        x46 = self.conv3_sub1_proj_bn(x46,   training=self.is_training) 
                                                 
        
        x45 = tf.image.resize(x45,size=tf.shape(x46)[1:3], method=tf.image.ResizeMethod.BILINEAR)
        x47 = self.sub12_sum([x45,x46])
        x47 = sub12_sum_relu(x47)
        x47 = self.interp(x47, z_factor=2.0)
        x47 = self.conv6_cls(x47)
                                          
        x48 = self.sub4_out(x41)
                                          
        x49 = self.sub24_out(x44)    
        return x47, x48, x49                             
                                          