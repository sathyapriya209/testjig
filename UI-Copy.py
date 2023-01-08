UI = '''
ScreenManager:
    Main:
    TESTScreen:
    CTC_ConfigurationScreen:
    Calibration_ConfigurationScreen:
    MPC_ConfigurationScreen:
    Logo:
<Logo>:
    name:'logo'
    orientation: "vertical"
    Image:
        id: gif
        source: 'firstpage.bmp'
        pos: self.pos
        size_hint: None, None
        size: root.size
        allow_stretch: True
        keep_ratio: False        
<Main>:
    name : 'BT setting'
    FloatLayout:
        orientation: "vertical"
        padding:(0,10,0,0)
        spacing:10
        MDToolbar:
            md_bg_color: 0, 0,0.7,0.7
            pos_hint :{'center_x':.42, 'center_y':.9}
            size_hint: 0.8,0.1
            canvas:
                Rectangle:
                    source: 'boAt.jpeg'
                    pos: (((self.parent.size[0])/2)+400,self.pos[1])
                    size: (120, 70)
            MDLabel:
                text: "bo"
                font_size: '40sp'
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos: (((self.parent.size[0])/2)-100,self.pos[1])
            MDLabel:
                text: "A"
                font_size: '40sp'
                theme_text_color: "Custom"
                text_color: (1,0,0,1)
                pos: (((self.parent.size[0])/2)-55,self.pos[1])
            MDLabel:
                text: "t Golem"
                font_size: '40sp'
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos: (((self.parent.size[0])/2)-25,self.pos[1])
        FloatLayout:
            canvas:
                Color:
                    rgba: 0, 0,0.7,0.7
                Rectangle:
                    pos: (30,30)
                    size: (1050, 550)
            MDTextFieldRect:
                id: DeviceName
                multiline: False
                hint_text: "Please Enter The Device Name to Connect"
                height: "60dp"
                md_bg_color: 1,1,1,1
                color_mode: 'custom'
                icon_right_color: app.theme_cls.primary_color
                icon_right: 'equal-box'
                pos_hint :{'center_x':.49, 'center_y':.75}
                size_hint: 0.9,None
            MDTextFieldRect:
                id: Firmware_or_CRC
                multiline: False
                hint_text: "Please Enter The Firmware version or CRC"
                height: "60dp"
                md_bg_color: 1,1,1,1
                color_mode: 'custom'
                icon_right_color: app.theme_cls.primary_color
                icon_right: 'equal-box'
                pos_hint :{'center_x':.49, 'center_y':.65}
                size_hint: 0.9,None
            MDRaisedButton:
                id:ConnectBt
                text: "Connect BT device"
                theme_text_color: "Custom"
                md_bg_color: 1,1,1,1
                text_color: (255,255,255,255)
                pos_hint :{'center_x':0.105, 'center_y':.55}
                on_press: app.connect()            
<TESTScreen>:
    name : 'Test'
    FloatLayout:
        orientation: "vertical"
        padding:(0,10,0,0)
        MDToolbar:
            md_bg_color: 0, 0,0.7,0.7
            pos_hint :{'center_x':.42, 'center_y':.9}
            size_hint: 0.8,0.1
            canvas:
                Rectangle:
                    source: 'boAt.jpeg'
                    pos: (((self.parent.size[0])/2)+400,self.pos[1])
                    size: (120, 70)
            MDLabel:
                text: "bo"
                font_size: '40sp'
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos: (((self.parent.size[0])/2)-100,self.pos[1])
            MDLabel:
                text: "A"
                font_size: '40sp'
                theme_text_color: "Custom"
                text_color: (1,0,0,1)
                pos: (((self.parent.size[0])/2)-55,self.pos[1])
            MDLabel:
                text: "t Golem"
                font_size: '40sp'
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos: (((self.parent.size[0])/2)-25,self.pos[1])
        FloatLayout:
            canvas:
                Color:
                    rgba: 0, 0,0.7,0.7
                Rectangle:
                    pos: (30,30)
                    size: (1050, 550)
            MDToolbar:
                title:"Select Test Cases"
                anchor_title: "center"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.4, 'center_y':.76}
                size_hint: 0.7,0.085                
            MDRaisedButton:
                id:back
                text: "Disconnect"
                theme_text_color: "Custom"
                md_bg_color: 1, 1, 1, 1
                text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.6, 'center_y':.625}
                on_press: app.Disconnect()
            MDRaisedButton:
                id:Clear
                text: "Clear"
                theme_text_color: "Custom"
                md_bg_color: 1, 1, 1, 1
                text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.75, 'center_y':.625}
                on_press: app.ClearAllConfiguration()
            MDRaisedButton:
                id:Calibration
                text: "CTC Calibration"
                theme_text_color: "Custom"
                md_bg_color: 1, 1, 1, 1
                text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.9, 'center_y':.625}
                on_press: app.CTC_Calibration()
            MDCheckbox:
                id:Speakercheck
                color:1,1,1
                md_bg_color: 1, 1, 1, 1
                on_active: root.checkbox_click_speakertesting(self, self.active,"Speker Test")
                size_hint: None, None
                size: "20dp", "20dp"
                pos_hint :{'center_x':.06, 'center_y':.660}
            MDToolbar:
                id:Speakertest
                title:"Speaker Testing"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.3, 'center_y':.660}
                size_hint: 0.4,0.05
            MDCheckbox:
                id:CTCcheck
                color:1,1,1
                md_bg_color: 1, 1, 1, 1
                on_active: root.checkbox_click_ctc(self, self.active,"CTC Test")
                size_hint: None, None
                size: "20dp", "20dp"
                pos_hint :{'center_x':.06, 'center_y':.590}
                on_press: app.OpenCTC()
            MDToolbar:
                id:CTCtest
                title:"CTC Testing"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.3, 'center_y':.590}
                size_hint: 0.4,0.05
            MDCheckbox:
                id:AudioTestingcheck
                color:1,1,1
                md_bg_color: 1, 1, 1, 1
                on_active: root.checkbox_click_audiotesting(self, self.active,"Mic Testing")
                size_hint: None, None
                size: "20dp", "20dp"
                pos_hint :{'center_x':.06, 'center_y':.520}
                on_press: app.AudioTestingconfigration()
            MDToolbar:
                id:Audiotest
                title:"Mic Test"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.3, 'center_y':.520}
                size_hint: 0.4,0.05
            MDCheckbox:
                id:BatteryLifecheck
                color:1,1,1
                md_bg_color: 1, 1, 1, 1
                on_active: root.checkbox_click_battery(self, self.active,"Battery Life Testing")
                size_hint: None, None
                size: "20dp", "20dp"
                pos_hint :{'center_x':.06, 'center_y':.450}
                on_press: app.BatteryLifeTestingconfigration()
            MDToolbar:
                id:BatteryLifetest
                title:"Battery Life Test"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.3, 'center_y':.450}
                size_hint: 0.4,0.05
            MDCheckbox:
                id:ConnectivityCheck
                color:1,1,1
                md_bg_color: 1, 1, 1, 1
                on_active: root.checkbox_click_bt(self, self.active,"Connectivity")
                size_hint: None, None
                size: "20dp", "20dp"
                pos_hint :{'center_x':.06, 'center_y':.380}
                on_press: app.Connectivityconfigration()
            MDToolbar:
                id:ConnectivityTest
                title:"Connectivity"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.25, 'center_y':.380}
                size_hint: 0.3,0.05
            MDCheckbox:
                id:Lngcheck
                color:1,1,1
                md_bg_color: 1, 1, 1, 1
                on_active: root.checkbox_click_lnghr(self, self.active,"Long Hour Playback")
                size_hint: None, None
                size: "20dp", "20dp"
                pos_hint :{'center_x':.06, 'center_y':.310}
                on_press: app.LongHourconfigration()
            MDToolbar:
                id:LngTest
                title:"Long Hour Test"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.25, 'center_y':.310}
                size_hint: 0.3,0.05
            MDCheckbox:
                id:rssicheck
                color:1,1,1
                md_bg_color: 1, 1, 1, 1
                on_active: root.checkbox_click_rssi(self, self.active,"Rssi Test")
                size_hint: None, None
                size: "20dp", "20dp"
                pos_hint :{'center_x':.06, 'center_y':.240}
                on_press: app.rssiconfigration()
            MDToolbar:
                id:RssiTest
                title:"Rssi Test"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.25, 'center_y':.240}
                size_hint: 0.3,0.05
            MDCheckbox:
                id:MPControlcheck
                color:1,1,1
                md_bg_color: 1, 1, 1, 1
                on_active: root.checkbox_click_mpcontrol(self, self.active,"Mobile Control")
                size_hint: None, None
                size: "20dp", "20dp"
                pos_hint :{'center_x':.06, 'center_y':.170}
                on_press: app.OpenMobilePhoneControl()
            MDToolbar:
                id:MPControlTest
                title:"Control via Mobile Phone"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.25, 'center_y':.170}
                size_hint: 0.3,0.05
            MDTextFieldRect:
                id: sumtext
                text:"Test Summary"
                multiline: True
                height: "20dp"
                md_bg_color: 0,0,0,0
                color_mode: 'custom'
                icon_right_color: app.theme_cls.primary_color                
                pos_hint :{'center_x':.75, 'center_y':.325}
                size_hint: 0.425,0.475
            MDRaisedButton:
                id:start
                text: "Start Test"
                theme_text_color: "Custom"
                md_bg_color: 1, 1, 1, 1
                text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.14, 'center_y':.095}
                on_press: app.GolemStartTest()
            MDRaisedButton:
                id:stoptest
                text: "Stop Test"
                theme_text_color: "Custom"
                md_bg_color: 1, 1, 1, 1
                text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.3, 'center_y':.095}
                on_press: app.Stop_test()            
<CTC_ConfigurationScreen>:
    name : 'CTC'
    FloatLayout:
        orientation: "vertical"
        padding:(0,10,0,0)
        MDToolbar:
            md_bg_color: 0, 0,0.7,0.7
            pos_hint :{'center_x':.42, 'center_y':.9}
            size_hint: 0.8,0.1
            canvas:
                Rectangle:
                    source: 'boAt.jpeg'
                    pos: (((self.parent.size[0])/2)+400,self.pos[1])
                    size: (120, 70)
            MDLabel:
                text: "bo"
                font_size: '40sp'
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos: (((self.parent.size[0])/2)-100,self.pos[1])
            MDLabel:
                text: "A"
                font_size: '40sp'
                theme_text_color: "Custom"
                text_color: (1,0,0,1)
                pos: (((self.parent.size[0])/2)-55,self.pos[1])
            MDLabel:
                text: "t Golem"
                font_size: '40sp'
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos: (((self.parent.size[0])/2)-25,self.pos[1])
        FloatLayout:
            canvas:
                Color:
                    rgba: 0, 0,0.7,0.7
                Rectangle:
                    pos: (30,30)
                    size: (1050, 550)
            MDToolbar:
                title:"CTC Test Cases List"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.4, 'center_y':.75}
                size_hint: 0.7,0.09            
            MDCheckbox:
                id:LeftEarbudSTCheck
                color:1,1,1
                md_bg_color: 1, 1, 1, 1
                on_active: root.checkbox_click_leftst(self, self.active,"Left Earbud - Play/Pause")
                size_hint: None, None
                size: "20dp", "20dp"
                pos_hint :{'center_x':.06, 'center_y':.6}
                on_press: app.ctc_leftst_configration()
            MDToolbar:
                id:LeftEarbudSTtest
                title:"Left Earbud - Play/Pause"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.25, 'center_y':.6}
                size_hint: 0.3,0.05
            MDCheckbox:
                id:LeftEarbudDTCheck
                color:1,1,1
                md_bg_color: 1, 1, 1, 1
                on_active: root.checkbox_click_leftdt(self, self.active,"Left Earbud - Previous")
                size_hint: None, None
                size: "20dp", "20dp"
                pos_hint :{'center_x':.06, 'center_y':.5}
                on_press: app.ctc_leftdt_configration()
            MDToolbar:
                id:LeftEarbudDTtest
                title:"Left Earbud - Previous"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.25, 'center_y':.5}
                size_hint: 0.3,0.05            
            MDCheckbox:
                id:RightEarbudSTCheck
                color:1,1,1
                md_bg_color: 1, 1, 1, 1
                on_active: root.checkbox_click_rightst(self, self.active,"Right Earbud - Play/Pause")
                size_hint: None, None
                size: "20dp", "20dp"
                pos_hint :{'center_x':.56, 'center_y':.6}
                on_press: app.ctc_rightst_configration()
            MDToolbar:
                id:RightEarbudSTtest
                title:"Right Earbud - Play/Pause"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.75, 'center_y':.6}
                size_hint: 0.3,0.05
            MDCheckbox:
                id:RightEarbudDTCheck
                color:1,1,1
                md_bg_color: 1, 1, 1, 1
                on_active: root.checkbox_click_rightdt(self, self.active,"Right Earbud - Next")
                size_hint: None, None
                size: "20dp", "20dp"
                pos_hint :{'center_x':.56, 'center_y':.5}
                on_press: app.ctc_rightdt_configration()
            MDToolbar:
                id:RightEarbudDTtest
                title:"Right Earbud - Next"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.75, 'center_y':.5}
                size_hint: 0.3,0.05
                        
            MDRaisedButton:
                id:SubmitConfiguration
                text: "Submit"
                theme_text_color: "Custom"
                md_bg_color: 1, 1, 1, 1
                text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.15, 'center_y':.2}
                on_press: app.doCtcTest()
            MDRaisedButton:
                id:CancelConfiguration
                text: "Cancel"
                theme_text_color: "Custom"
                md_bg_color: 1, 1, 1, 1
                text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.3, 'center_y':.2}
                on_press: app.configration1()
<MPC_ConfigurationScreen>:
    name : 'MobilePhoneControl'
    FloatLayout:
        orientation: "vertical"
        padding:(0,10,0,0)
        MDToolbar:
            md_bg_color: 0, 0,0.7,0.7
            pos_hint :{'center_x':.42, 'center_y':.9}
            size_hint: 0.8,0.1
            canvas:
                Rectangle:
                    source: 'boAt.jpeg'
                    pos: (((self.parent.size[0])/2)+400,self.pos[1])
                    size: (120, 70)
            MDLabel:
                text: "bo"
                font_size: '40sp'
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos: (((self.parent.size[0])/2)-100,self.pos[1])
            MDLabel:
                text: "A"
                font_size: '40sp'
                theme_text_color: "Custom"
                text_color: (1,0,0,1)
                pos: (((self.parent.size[0])/2)-55,self.pos[1])
            MDLabel:
                text: "t Golem"
                font_size: '40sp'
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos: (((self.parent.size[0])/2)-25,self.pos[1])
        FloatLayout:
            canvas:
                Color:
                    rgba: 0, 0,0.7,0.7
                Rectangle:
                    pos: (30,30)
                    size: (1050, 550)
            MDToolbar:
                title:"MobilePhone Control Test Cases List"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.4, 'center_y':.75}
                size_hint: 0.7,0.09            
            MDCheckbox:
                id:CallControlCheck
                color:1,1,1
                md_bg_color: 1, 1, 1, 1
                on_active: root.checkbox_click_CallControl(self, self.active,"Call Control")
                size_hint: None, None
                size: "20dp", "20dp"
                pos_hint :{'center_x':.06, 'center_y':.6}
                on_press: app.ctc_callcontrol_configration()
            MDToolbar:
                id:CallControltest
                title:"Call Control"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.25, 'center_y':.6}
                size_hint: 0.3,0.05                        
            MDCheckbox:
                id:PlayControlCheck
                color:1,1,1
                md_bg_color: 1, 1, 1, 1
                on_active: root.checkbox_click_PlayControl(self, self.active,"Play Control")
                size_hint: None, None
                size: "20dp", "20dp"
                pos_hint :{'center_x':.56, 'center_y':.6}
                on_press: app.ctc_playcontrol_configration()
            MDToolbar:
                id:PlayControltest
                title:"Play Control"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.75, 'center_y':.6}
                size_hint: 0.3,0.05
            MDRaisedButton:
                id:SubmitConfiguration
                text: "Submit"
                theme_text_color: "Custom"
                md_bg_color: 1, 1, 1, 1
                text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.15, 'center_y':.2}
                on_press: app.doMobilePhoneControlTest()
            MDRaisedButton:
                id:CancelConfiguration
                text: "Cancel"
                theme_text_color: "Custom"
                md_bg_color: 1, 1, 1, 1
                text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.3, 'center_y':.2}
                on_press: app.configration2()                
<Calibration_ConfigurationScreen>:
    name : 'Calibration'
    FloatLayout:
        orientation: "vertical"
        padding:(0,10,0,0)
        MDToolbar:
            md_bg_color: 0, 0,0.7,0.7
            pos_hint :{'center_x':.42, 'center_y':.9}
            size_hint: 0.8,0.1
            canvas:
                Rectangle:
                    source: 'boAt.jpeg'
                    pos: (((self.parent.size[0])/2)+400,self.pos[1])
                    size: (120, 70)
            MDLabel:
                text: "bo"
                font_size: '40sp'
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos: (((self.parent.size[0])/2)-100,self.pos[1])
            MDLabel:
                text: "A"
                font_size: '40sp'
                theme_text_color: "Custom"
                text_color: (1,0,0,1)
                pos: (((self.parent.size[0])/2)-55,self.pos[1])
            MDLabel:
                text: "t Golem"
                font_size: '40sp'
                theme_text_color: "Custom"
                text_color: 1, 1, 1, 1
                pos: (((self.parent.size[0])/2)-25,self.pos[1])
        FloatLayout:
            canvas:
                Color:
                    rgba: 0, 0,0.7,0.7
                Rectangle:
                    pos: (30,30)
                    size: (1050, 550)
            MDToolbar:
                title:"Calibration Options"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.4, 'center_y':.75}
                size_hint: 0.7,0.09            
            MDCheckbox:
                id:LeftEarbudCaliCheck
                color:1,1,1
                md_bg_color: 1, 1, 1, 1
                on_active: root.checkbox_click_leftCali(self, self.active,"Left Earbud - Calibration")
                size_hint: None, None
                size: "20dp", "20dp"
                pos_hint :{'center_x':.06, 'center_y':.6}
                on_press: app.LeftEarbudCalibrationCheck()
            MDToolbar:
                id:LeftEarbudCalitest
                title:"Left Earbud - Calibration"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.25, 'center_y':.6}
                size_hint: 0.3,0.05
            MDCheckbox:
                id:RightEarbudCaliCheck
                color:1,1,1
                md_bg_color: 1, 1, 1, 1
                on_active: root.checkbox_click_rightCali(self, self.active,"Right Earbud - Calibration")
                size_hint: None, None
                size: "20dp", "20dp"
                pos_hint :{'center_x':.56, 'center_y':.6}
                on_press: app.RightEarbudCalibrationCheck()
            MDToolbar:
                id:RightEarbudCalitest
                title:"Right Earbud - Calibration"
                md_bg_color: 1,1,1,1
                specific_text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.75, 'center_y':.6}
                size_hint: 0.3,0.05
            MDRaisedButton:
                id:StartCalibration
                text: "Start"
                theme_text_color: "Custom"
                md_bg_color: 1, 1, 1, 1
                text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.15, 'center_y':.2}
                on_press: app.StartCalibration()
            MDRaisedButton:
                id:StopCalibration
                text: "Stop"
                theme_text_color: "Custom"
                md_bg_color: 1, 1, 1, 1
                text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.3, 'center_y':.2}
                on_press: app.StopCalibration()
            MDRaisedButton:
                id:CancelCalibration
                text: "Cancel"
                theme_text_color: "Custom"
                md_bg_color: 1, 1, 1, 1
                text_color: 255, 255, 255, 255
                pos_hint :{'center_x':.45, 'center_y':.2}
                on_press: app.CancelCalibration()        
<CtcDialogLeftStConfig>:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"
    MDTextField:
        id:LeftStNoOfTimes
        hint_text: "Please enter number of times"
        text_color:self.theme_cls.primary_color
        on_text: app.leftstNoOfTimes = self.text
    MDTextField:
        id:LeftstInterval
        hint_text: "Please enter Interval between Touch"
        text_color:self.theme_cls.primary_color
        on_text: app.leftstInterval = self.text

<CtcDialogLeftDtConfig>:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"
    MDTextField:
        id:LeftdtNoOfTimes
        hint_text: "Please enter number of times"
        text_color:self.theme_cls.primary_color
        on_text: app.leftdtNoOfTimes = self.text
    MDTextField:
        id:LeftdtInterval
        hint_text: "Please enter Interval between Touch"
        text_color:self.theme_cls.primary_color
        on_text: app.leftdtInterval = self.text
<CtcDialogLeftLtConfig>:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"
    MDTextField:
        id:LeftltNoOfTimes
        hint_text: "Please enter number of times"
        text_color:self.theme_cls.primary_color
        on_text: app.leftltNoOfTimes = self.text
    MDTextField:
        id:LeftltInterval
        hint_text: "Please enter Interval between Touch"
        text_color:self.theme_cls.primary_color
        on_text: app.leftltInterval = self.text

<CtcDialogRightStConfig>:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"
    MDTextField:
        id:RightstNoOfTimes
        hint_text: "Please enter number of times"
        text_color:self.theme_cls.primary_color
        on_text: app.rightstNoOfTimes = self.text
    MDTextField:
        id:RightstInterval
        hint_text: "Please enter Interval between Touch"
        text_color:self.theme_cls.primary_color
        on_text: app.rightstInterval = self.text

<CtcDialogRightDtConfig>:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"
    MDTextField:
        id:RightdtNoOfTimes
        hint_text: "Please enter number of times"
        text_color:self.theme_cls.primary_color
        on_text: app.rightdtNoOfTimes = self.text
    MDTextField:
        id:RightdtInterval
        hint_text: "Please enter Interval between Touch"
        text_color:self.theme_cls.primary_color
        on_text: app.rightdtInterval = self.text
<CtcDialogRightLtConfig>:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"
    MDTextField:
        id:RightltNoOfTimes
        hint_text: "Please enter number of times"
        text_color:self.theme_cls.primary_color
        on_text: app.rightltNoOfTimes = self.text
    MDTextField:
        id:RightltInterval
        hint_text: "Please enter Interval between Touch"
        text_color:self.theme_cls.primary_color
        on_text: app.rightltInterval = self.text
        
<LnghrConfig>:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"
    MDTextField:
        id:LngCon
        hint_text: "Please enter playback Minutes"
        text_color:self.theme_cls.primary_color
        on_text: app.Lnghr = self.text
    MDTextField:
        id:LngCon
        hint_text: "Please enter the volume"
        text_color:self.theme_cls.primary_color
        on_text: app.Lnghrvolume = self.text
<RssiConfig>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "60dp"    
    MDTextField:
        id:LngCon
        hint_text: "Please enter time duration for Rssi observation in seconds"
        text_color:self.theme_cls.primary_color
        on_text: app.rssiduration = self.text
<BtConfig>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"    
    MDTextField:
        id:LngCon
        hint_text: "Please enter number of times for BT pairing - Testing"
        text_color:self.theme_cls.primary_color
        on_text: app.btpair = self.text
    MDTextField:
        id:LngCon
        hint_text: "Please enter number of times for BT connection - Testing"
        text_color:self.theme_cls.primary_color
        on_text: app.bt = self.text        
<CallControlDialog>:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"
    MDTextField:
        id:CallAns_EndNoOfTimes
        hint_text: "Please enter number of times for Answer Call and End"
        text_color:self.theme_cls.primary_color
        on_text: app.CallAns_EndNoOfTimes = self.text
    MDTextField:
        id:CallRejectNoOfTimes
        hint_text: "Please enter number of times for Answer Reject"
        text_color:self.theme_cls.primary_color
        on_text: app.CallRejectNoOfTimes = self.text
<PlayControlDialog>:
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "180dp"
    MDTextField:
        id:PlayControlPlayPauseNoOfTimes
        hint_text: "Please enter number of times for Play/Pause"
        text_color:self.theme_cls.primary_color
        on_text: app.PlayControlPlayPauseNoOfTimes = self.text
    MDTextField:
        id:PlayControlNextPrevNoOfTimes
        hint_text: "Please enter number of times for Next/Previous"
        text_color:self.theme_cls.primary_color
        on_text: app.PlayControlNextPrevNoOfTimes = self.text
    MDTextField:
        id:PlayControlVolumeUpDownNoOfTimes
        hint_text: "Please enter number of times for Volume Up/Down"
        text_color:self.theme_cls.primary_color
        on_text: app.PlayControlVolumeUpDownNoOfTimes = self.text
'''
