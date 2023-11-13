#pragma once

#include <vector>



namespace DAGGER{

	template<class i_t, class f_t, class CON_T, class DATA_T, class PARAM_T>
	class TinySubGraph
	{
	public:
		TinySubGraph(){};
		TinySubGraph(CON_T& con, DATA_T& data, PARAM_T& param){
			this->con = &con;
			this->data = &data;
			this->param = &param;
			this->isDone = std::vector<std::uint8_t>(this->con->nxy(), false);
		};

		~TinySubGraph(){};

		CON_T* con;
		DATA_T* data;
		PARAM_T* param;

		std::vector<i_t> stack;
		std::vector<i_t> nodes;
		std::vector<i_t> baseLevels;
		std::vector<std::uint8_t> isDone;

		template<class CONTAINER_INT>
		void build_simple(CONTAINER& startingNodes){

			this->stack.clear();
			this->nodes.clear();
			this->baseLevels.clear();

			// Initialising a node queue
			std::queue<i_t> tQ;

			// Feeding it witht the starting nodes
			for(auto v:startingNodes){
				nodes.emplace_back();
				isDone[v] = true;
				tQ.emplace(v);
			}



		}

		
	};


















}