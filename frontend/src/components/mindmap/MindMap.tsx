import React, { useEffect, useState, useCallback } from 'react';
import ReactFlow, {
  Node,
  Edge,
  Controls,
  Background,
  useNodesState,
  useEdgesState,
  MarkerType,
  BackgroundVariant,
} from 'reactflow';
import 'reactflow/dist/style.css';
import { Term } from '../../types/term';
import { termsApi } from '../../services/api';
import CustomNode from './CustomNode';
import dagre from 'dagre';

const nodeTypes = {
  custom: CustomNode,
};

const getLayoutedElements = (nodes: Node[], edges: Edge[]) => {
  const dagreGraph = new dagre.graphlib.Graph();
  dagreGraph.setDefaultEdgeLabel(() => ({}));
  dagreGraph.setGraph({ rankdir: 'TB', ranksep: 100, nodesep: 150 });

  nodes.forEach((node) => {
    dagreGraph.setNode(node.id, { width: 200, height: 50 });
  });

  edges.forEach((edge) => {
    dagreGraph.setEdge(edge.source, edge.target);
  });

  dagre.layout(dagreGraph);

  const layoutedNodes = nodes.map((node) => {
    const nodeWithPosition = dagreGraph.node(node.id);
    return {
      ...node,
      position: {
        x: nodeWithPosition.x - 100,
        y: nodeWithPosition.y - 25,
      },
    };
  });

  return { nodes: layoutedNodes, edges };
};

const MindMap: React.FC = () => {
  const [nodes, setNodes, onNodesChange] = useNodesState([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    loadGraphData();
  }, []);

  const loadGraphData = async () => {
    try {
      setLoading(true);
      const response = await termsApi.getAllTerms();
      const terms = response.items;

      // Создаем узлы
      const newNodes: Node[] = terms.map((term) => ({
        id: term.id,
        type: 'custom',
        data: {
          label: term.term,
          isCenter: term.id === 'электронный_документ', // Центральный узел
        },
        position: { x: 0, y: 0 }, // Будет пересчитано
      }));

      // Создаем связи
      const newEdges: Edge[] = [];
      terms.forEach((term) => {
        term.relations.forEach((relation) => {
          newEdges.push({
            id: `${term.id}-${relation.target_term_id}`,
            source: term.id,
            target: relation.target_term_id,
            label: relation.relation_type,
            type: 'smoothstep',
            animated: false,
            style: { stroke: '#9d174d', strokeWidth: 2 },
            labelStyle: { fill: '#4b5563', fontSize: 10, fontWeight: 500 },
            labelBgStyle: { fill: '#fdf2f8', fillOpacity: 0.9 },
            markerEnd: {
              type: MarkerType.ArrowClosed,
              color: '#9d174d',
            },
          });
        });
      });

      // Применяем автоматическую раскладку
      const { nodes: layoutedNodes, edges: layoutedEdges } = getLayoutedElements(
        newNodes,
        newEdges
      );

      setNodes(layoutedNodes);
      setEdges(layoutedEdges);
    } catch (error) {
      console.error('Error loading graph data:', error);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="text-gray-600">Загрузка графа...</div>
      </div>
    );
  }

  return (
    <div style={{ width: '100%', height: 'calc(100vh - 64px)' }}>
      <ReactFlow
        nodes={nodes}
        edges={edges}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        nodeTypes={nodeTypes}
        fitView
        attributionPosition="bottom-left"
      >
        <Controls />
        <Background variant={BackgroundVariant.Dots} gap={12} size={1} color="#f9a8d4" />
      </ReactFlow>
    </div>
  );
};

export default MindMap;
