Vim�UnDo� ��6=+�)��лԿ�\��>\���褻  %                                   _�x    _�                    �        ����                                                                                                                                                                                                                                                                                                                            �           �           V        _�i     �   �   �          <<<<<<< HEAD   #    public init(page: Binding<Int>,                    data: [Element],   )                id: KeyPath<Element, ID>,   H                @ViewBuilder content: @escaping (Element) -> PageView) {   =======5�_�                    �        ����                                                                                                                                                                                                                                                                                                                            �           �           V        _�j    �   �   �          >>>>>>> upstream/master5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �           �           V        _�j    �  ,  .          #endif�  +  -          }�  *  ,              }�  )  +          (        TestContent(color: Color.yellow)�  (  *          $    static var previews: some View {�  '  )          (struct Pager_Previews: PreviewProvider {�  &  (          :@available(iOS 14.0, OSX 10.15, tvOS 13.0, watchOS 6.0, *)�  %  '           �  $  &          }�  #  %              }�  "  $          	        }�  !  #                  .vertical()�     "          ,        .swipeInteractionArea(.allAvailable)�    !                       }�                �              %                 self.coffset = value�              %        .onOffsetChanged() { value in�              
        })�                          .background(color)�              Z            .frame(width: UIScreen.main.bounds.width, height: UIScreen.main.bounds.height)�              (            .edgesIgnoringSafeArea(.all)�                          view�              U        Pager(page: self.$index, data: data, offset: self.$offset, content: { view in�              '        Text("offset: \(self.coffset)")�                      VStack {�                      �                      �                      �              [        let data = [TextContent(text: "1"), TextContent(text: "2"), TextContent(text: "3")]�                  var body: some View {�                  �                  var color: Color = .blue�              %    @State var coffset = CGFloat.zero�              $    @State var offset = CGPoint.zero�  
                @State var index: Int = 0�  	            struct TestContent: View {�    
          :@available(iOS 14.0, OSX 10.15, tvOS 13.0, watchOS 6.0, *)�    	           �              }�                  }�                      return Text(text)�                  var body: some View {�                  �                  var text: String�                   var id = UUID()�   �            3struct TextContent: View, Identifiable, Equatable {�   �             	#if DEBUG�   �   �           �   �   �          }�   �   �           �   �   �              }�   �   �          >>>>>>> upstream/master�   �   �          S        self.init(page: page, data: Array(data), id: \Element.id, content: content)�   �   �          �    public init<Data: RandomAccessCollection>(page: Binding<Int>, data: Data, @ViewBuilder content: @escaping (Element) -> PageView) where Data.Index == Int, Data.Element == Element {�   �   �          =======�   �   �          L        self.init(page: page, data: data, id: \Element.id, content: content)�   �   �          H                @ViewBuilder content: @escaping (Element) -> PageView) {�   �   �          )                offset: Binding<CGPoint>,�   �   �                           data: [Element],�   �   �          #    public init(page: Binding<Int>,�   �   �          <<<<<<< HEAD�   �   �          >    /// - Parameter content: Factory method to build new pages�   �   �          E    /// - Parameter data: Collection of items to populate the content�   �   �              ///�   �   �               /// Initializes a new Pager.�   �   �           �   �   �          @extension Pager where ID == Element.ID, Element : Identifiable {�   �   �          :@available(iOS 14.0, OSX 10.15, tvOS 13.0, watchOS 6.0, *)�   �   �           �   �   �          }�   �   �           �   �   �              }�   �   �                  return pagerContent�   �   �           �   �   �          	        }�   �   �          L            pagerContent = pagerContent.preferredItemSize(preferredItemSize)�   �   �          6        if let preferredItemSize = preferredItemSize {�   �   �           �   �   �          N        pagerContent = shouldRotate ? pagerContent.rotation3D() : pagerContent�   �   �          �        pagerContent = isHorizontal ? pagerContent.horizontal(horizontalSwipeDirection) : pagerContent.vertical(verticalSwipeDirection)�   �   �          b        pagerContent = allowsMultiplePagination ? pagerContent.multiplePagination() : pagerContent�   �   �           �   �   �                    #endif�   �   �          %            .sensitivity(sensitivity)�   �   �          )            .delaysTouches(delaysTouches)�   �   �          ,            .pagingPriority(gesturePriority)�   �   �          +            .allowsDragging(allowsDragging)�   �   �          7            .swipeInteractionArea(swipeInteractionArea)�   �   �          %          pagerContent = pagerContent�   �   �                  #if !os(tvOS)�   �   �           �   �   �          1                .pagingAnimation(pagingAnimation)�   �   �          $                .padding(sideInsets)�   �   �          %				.onDraggingBegan(onDraggingBegan)�   �   �          1                .onOffsetChanged(onOffsetChanged)�   �   �          -                .onPageChanged(onPageChanged)�   �   �          K                .itemAspectRatio(itemAspectRatio, alignment: itemAlignment)�   �   �          )                .itemSpacing(itemSpacing)�   �   �          '                .pageOffset(pageOffset)�   �   �          .                .interactive(interactiveScale)�   �   �          %                .alignment(alignment)�   �   �          E                .loopPages(isInifinitePager, repeating: loopingCount)�   �   �          ;                .contentLoadingPolicy(contentLoadingPolicy)�   �   �          *                         content: content)�   �   �                                    id: id,�   �   �          $                         data: data,�   �   �          %                         page: $page,�   �   �          $            PagerContent(size: size,�   �   �                  var pagerContent =�   �   �          4    func content(for size: CGSize) -> PagerContent {�   �   �           �   �   �              }�   �   �                  .clipped()�   �   �          	        }�   �   �                          })�   �   �                              �   �   �          0                    self.onOffsetChanged?(value)�   �   �          F                .onChange(of: self.draggingOffset, perform: { value in�   �   �          )            self.content(for: proxy.size)�   �   �          !        GeometryReader { proxy in�   �   �               public var body: some View {�   �   �           �   �   �              }�   �   �                  self.content = content�   �   �                  self.id = id�   �   �                  self.data = Array(data)�   �   �                  self._page = page�   �   �          �    public init<Data: RandomAccessCollection>(page: Binding<Int>, data: Data, id: KeyPath<Element, ID>, @ViewBuilder content: @escaping (Element) -> PageView) where Data.Index == Int, Data.Element == Element {�   �   �          >    /// - Parameter content: Factory method to build new pages�   �   �          8    /// - Parameter id: KeyPath to identifiable property�   �   �          E    /// - Parameter data: Collection of items to populate the content�   �   �          3    /// - Parameter page: Binding to the page index�   �   �              ///�   �   �          "    /// Initializes a new `Pager`.�   �   �              �   �   �              }�   �   �          	        }�   �   �                       onPageChanged?(page)�   �   �                  didSet {�   �   �              @Binding var page: Int {�   �   �              /// Page index�   �   �           �   �   �               @State var pageIncrement = 1�   �   �          /    /// Increment resulting from the last swipe�   �   �           �   �   �          +    @State var draggingVelocity: Double = 0�   �   �          -    /// `swipeGesture` velocity on the X-Axis�   �   �           �   �   �          
    #endif�   �   �          4    @State var lastDraggingValue: DragGesture.Value?�   �   �              #if !os(tvOS)�   �   �          5    /// `swipeGesture` last translation on the X-Axis�   �   �           �   �   �          *    @State var draggingOffset: CGFloat = 0�   �   �          0    /// `swipeGesture` translation on the X-Axis�   �   �           �   �   �          #    @State var size: CGSize = .zero�   �   �              /// Size of the view�   �   �           �   �   �          *    /*** State and Binding properties ***/�   �   �           �   �   �          #	var onDraggingBegan: (() -> Void)?�   �   �          &	/// Callback for when dragging begins�   �   �          	�   �   �          -    var onOffsetChanged: ((CGFloat) -> Void)?�   �   �          #    /// Callback for every new page�   �   �              �   �   �          '    var onPageChanged: ((Int) -> Void)?�   �   �          #    /// Callback for every new page�   �   �           �   �   �          "    var preferredItemSize: CGSize?�   �   �          0    /// Will try to have the items fit this size�   �   �           �      �          !    var itemAspectRatio: CGFloat?�   ~   �          f    /// Will apply this ratio to each page item. The aspect ratio follows the formula _width / height_�   }              �   |   ~          3    var gesturePriority: GesturePriority = .default�   {   }          /    /// Priority selected to add `swipeGesture`�   z   |           �   y   {          "    var delaysTouches: Bool = true�   x   z          1    /// Wheter `Pager` delays gesture recognition�   w   y           �   v   x          .    var allowsMultiplePagination: Bool = false�   u   w          :    /// Whether `Pager` should page multiple pages at once�   t   v           �   s   u              var loopingCount: UInt = 1�   r   t          N    /// Number of times the input data should be repeated in a looping `Pager`�   q   s           �   p   r          &    var isInifinitePager: Bool = false�   o   q          +    /// Whether the `Pager` loops endlessly�   n   p           �   m   o               var itemSpacing: CGFloat = 0�   l   n              /// Space between pages�   k   m           �   j   l              var sideInsets: CGFloat = 0�   i   k              /// Vertical padding�   h   j           �   g   i              var pageOffset: Double = 0�   f   h          7    /// Used to modify `Pager` offset outside this view�   e   g           �   d   f          "    var shouldRotate: Bool = false�   c   e          8    /// `true` if pages should have a 3D rotation effect�   b   d           �   a   c          #    var allowsDragging: Bool = true�   `   b          )    /// `true` if  `Pager` can be dragged�   _   a           �   ^   `          %    var interactiveScale: CGFloat = 1�   ]   _          ?    /// Shrink ratio that affects the items that aren't focused�   \   ^           �   [   ]          !    var isHorizontal: Bool = true�   Z   \          )    /// `true` if the pager is horizontal�   Y   [           �   X   Z          .    var alignment: PositionAlignment = .center�   W   Y          8    /// The elements alignment relative to the container�   V   X           �   U   W          2    var itemAlignment: PositionAlignment = .center�   T   V          %    /// Item alignment inside `Pager`�   S   U           �   R   T          :    var swipeInteractionArea: SwipeInteractionArea = .page�   Q   S              /// Hittable area�   P   R           �   O   Q          E    var verticalSwipeDirection: VerticalSwipeDirection = .topToBottom�   N   P          ,    /// Swipe direction for vertical `Pager`�   M   O           �   L   N          I    var horizontalSwipeDirection: HorizontalSwipeDirection = .leftToRight�   K   M          .    /// Swipe direction for horizontal `Pager`�   J   L           �   I   K          =    var contentLoadingPolicy: ContentLoadingPolicy = .default�   H   J          1    /// Policy to be applied when loading content�   G   I           �   F   H          5    var sensitivity: PaginationSensitivity = .default�   E   G          F    /// Sensitivity used to determine whether or not to swipe the page�   D   F           �   C   E          ;    var pagingAnimation: ((DragResult) -> PagingAnimation)?�   B   D          <    /// Animation to be applied when the user stops dragging�   A   C           �   @   B          %    /*** ViewModified properties ***/�   ?   A           �   >   @              var data: [Element]�   =   ?          3    /// Array of items that will populate each page�   <   >           �   ;   =               let id: KeyPath<Element, ID>�   :   <          %    /// `KeyPath` to data id property�   9   ;           �   8   :          &    let content: (Element) -> PageView�   7   9          /    /// `ViewBuilder` block to create each page�   6   8           �   5   7              /*** Dependencies ***/�   4   6           �   3   5          F    let rotationAxis: (x: CGFloat, y: CGFloat, z: CGFloat) = (0, 1, 0)�   2   4          +    /// Axis of rotation when should rotate�   1   3           �   0   2          /    let rotationInteractiveScale: CGFloat = 0.7�   /   1          ,    /// Angle of rotation when should rotate�   .   0           �   -   /          $    let rotationDegrees: Double = 20�   ,   .          ,    /// Angle of rotation when should rotate�   +   -           �   *   ,              /*** Constants ***/�   )   +           �   (   *              }�   '   )                  case backward�   &   (          &        /// Swiping from right to left�   %   '                  case forward�   $   &          '        /// Swiping  from left to right�   #   %              enum Direction {�   "   $          A    /// `Direction` determines the direction of the swipe gesture�   !   #           �       "          jpublic struct Pager<Element, ID, PageView>: View  where PageView: View, Element: Equatable, ID: Hashable {�      !          :@available(iOS 14.0, OSX 10.15, tvOS 13.0, watchOS 6.0, *)�                 ///�                5/// - 0.6 shrink ratio for items that aren't focused.�                /// - 30 px of vertical insets�                /// - 10 px beetween pages�                &/// This snippet creates a pager with:�                ///�                !///         .itemAspectRatio(0.6)�                ///         .padding(30)�                ///         .itemSpacing(10)�                ///     }).interactive(0.8)�                &///               self.pageView(index)�                !///           content: { index in�                ///           data: data,�                ///     Pager(page: $page�                ///�                /// # Example #�                ///�                �/// of view-modifier functions.  You can change the vertical insets, spacing between items, ... You can also make the pages size interactive.�                �/// this view will create a scrollable container to display a handful of pages. The pages are recycled on scroll. `Pager` is easily customizable through a number�                �/// `Pager` is a view built on top of native SwiftUI components. Given a `ViewBuilder` and some `Identifiable` and `Equatable` data,�   
             ///�   	              �      
          import SwiftUI�      	           �                //�                B//  Copyright © 2019 Fernando Moya de Rivas. All rights reserved.�                4//  Created by Fernando Moya de Rivas on 05/12/2019.�                //�                //  SwiftUIPager�                //  Pager.swift�                 //5�_�                    �        ����                                                                                                                                                                                                                                                                                                                            �          �          V       _�v     �   �   �          <<<<<<< HEAD   #    public init(page: Binding<Int>,                    data: [Element],   )                offset: Binding<CGPoint>,   H                @ViewBuilder content: @escaping (Element) -> PageView) {   L        self.init(page: page, data: data, id: \Element.id, content: content)   =======5�_�                     �        ����                                                                                                                                                                                                                                                                                                                            �          �          V       _�w    �   �   �          >>>>>>> upstream/master5�_�                    �        ����                                                                                                                                                                                                                                                                                                                                                             _�`     �   �   �        5�_�                    �        ����                                                                                                                                                                                                                                                                                                                                                             _�a     �   �   �        5�_�                     �        ����                                                                                                                                                                                                                                                                                                                                                             _�c     �   �   �        5��