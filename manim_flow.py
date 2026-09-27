from manim import *

class SGLangRadixAttentionScene(Scene):
    def construct(self):
        title = Text("SGLang RadixAttention: Dynamic Prefix Caching", font_size=34, color=BLUE).to_edge(UP)
        self.play(Write(title))

        root_node = Circle(radius=0.4, color=CYAN, fill_opacity=0.8).shift(UP * 1.2)
        root_label = Text("Root", font_size=20).move_to(root_node)
        self.play(GrowFromCenter(root_node), Write(root_label))

        child_sys = Rectangle(height=0.6, width=2.4, color=GREEN, fill_opacity=0.6).shift(LEFT * 2.8 + DOWN * 0.2)
        sys_label = Text("System Prompt (K=128)", font_size=16).move_to(child_sys)
        arr1 = Arrow(root_node.get_bottom(), child_sys.get_top(), buff=0.1, color=WHITE)
        self.play(GrowArrow(arr1), Create(child_sys), Write(sys_label))

        child_agent = Rectangle(height=0.6, width=2.4, color=PURPLE, fill_opacity=0.6).shift(RIGHT * 2.8 + DOWN * 0.2)
        agent_label = Text("Agent Turn 1 (K=256)", font_size=16).move_to(child_agent)
        arr2 = Arrow(root_node.get_bottom(), child_agent.get_top(), buff=0.1, color=WHITE)
        self.play(GrowArrow(arr2), Create(child_agent), Write(agent_label))

        stat_box = Rectangle(height=1.0, width=6.5, color=GOLD).to_edge(DOWN)
        stat_text = Text("Cache Hit: 88.4% | Latency Reduction: 4.8x | Zero KV Recompute", font_size=18, color=GOLD).move_to(stat_box)
        self.play(Create(stat_box), Write(stat_text))
        self.wait(2)
